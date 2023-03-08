from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm, KsrtcPassFormField, IrctcPassFormField
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorator import *
from .models import *
from ksrtc.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer', 'superadmin', 'admin'])

def dashPage(request):
    return render(request, 'userdashboard.html')

def UserProfilePage(request):

    return render (request, 'profile.html')

def notfoundPage(request):
    return render(request, '404.html')


def TestPage(request):
    return render(request, 'test.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dash')
        
        else:
            messages.info(request, 'Password Or Username is incorrect')
            

    return render(request, 'login.html')

# def registerPage(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'register.html', context)


@unauthenticated_user
def registerPage(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')


            group = Group.objects.get(name='customer') 
            user.groups.add(group)


            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('login')
    return render(request, 'userregister.html', {'form': form})



# def BusPassForm(request):
#     school = admindb.SchoolDetail.objects.all()
#     place = Place.objects.all()
#     subtime = SubTime.objects.all()
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         dob = request.POST.get("dob")
#         mobile = request.POST.get("mobile")
#         adhaar_no = request.POST.get("adhaar_no")
#         address = request.POST.get("address")
#         school_name = request.POST.get("school_name")
#         start_place = request.POST.get("start_place")
#         end_place = request.POST.get("end_place")
#         time_periode = request.POST.get("time_periode")
#         profileimage = request.FILES.get("profileimage")
#         idimage = request.FILES.get("idimage")
#         adhaar_image = request.FILES.get("adhaar_image")
#         try:
#             buspassform = PassForm(name=name, age=age, dob=dob, mobile=mobile, adhaar_no=adhaar_no, address=address, school_name=school_name, start_place=start_place, end_place=end_place, time_periode=time_periode, profileimage=profileimage, idimage=idimage, adhaar_image=adhaar_image)
#             buspassform.save()
#             messages.success(request, 'application submitted')
#             return redirect('dash')
#         except:
#             messages.error(request, 'Error in submitting your appliction')
#             return redirect('buspassform')
#         print(form.error)

        
#     return render(request, 'buspassform.html', {'school':school, 'place':place, 'subtime':subtime})



@login_required
def BusPassForm(request):
    user = request.user
    if request.method == 'POST':
        form = KsrtcPassFormField(request.POST, request.FILES)
        if form.is_valid():
            pass_form = form.save(commit=False)
            pass_form.user = user

            # Calculate the amount based on bus_rate and sub_time
            sub_time = pass_form.time_periode.sub_time
            bus_rate = pass_form.bus_rate
            amount = int(0.1 * bus_rate * sub_time)
            amount_inr = amount

            # Initialize the Razorpay client
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            # Create a new order
            order = client.order.create({
                'amount': amount * 100,  # Amount is in paisa
                'currency': 'INR',
                'payment_capture': '1'  # Auto-capture payment
            })

            # Save the order_id to the PassForm instance
            pass_form.order_id = order['id']
            pass_form.amount = amount
            pass_form.save()

            # Render the payment page with the order details
            return render(request, 'payment.html', {'order': order, 'amount_inr' : amount_inr})

        else:
            messages.error(request, 'Error in submitting your application')
            print(form.errors)

    else:
        form = KsrtcPassFormField(initial={'user': user})

    return render(request, 'buspassform.html', {'form': form, 'user': user})


@csrf_exempt
def razorpay_payment(request):
    if request.method == "POST":
        # Get the Razorpay payment details from the POST request
        order_id = request.POST.get('razorpay_order_id')
        payment_id = request.POST.get('razorpay_payment_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the signature to ensure that the request has come from Razorpay
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
        except:
            return JsonResponse({'status': 'failure'})

        # Get the PassForm instance for the current user and update the 'paid' field to True
        pass_form = PassForm.objects.filter(user=request.user, paid=False).first()
        if pass_form:
            pass_form.paid = True
            pass_form.order_id = order_id
            pass_form.save()

             # Get the school email from the PassForm instance
            school_email = pass_form.school_name.school_email

            # Send an email to the school email with the PassForm data and verification and cancel buttons
            context = {
                'pass_form': pass_form,
                'verification_url': 'https://yourwebsite.com/verify',
                'cancel_url': 'https://yourwebsite.com/cancel',
            }
            message = render_to_string('passform_email.html', context)
            send_mail(
                'Bus Pass Form',
                message,
                'your_email@example.com',
                [school_email],
                fail_silently=False,
            )

        return JsonResponse({'status': 'success'})


@login_required
def view_pass_forms(request):
    user = request.user
    pass_forms = PassForm.objects.filter(user=user)
    return render(request, 'viewpassforms.html', {'pass_forms': pass_forms})


def TrainPassForm(request):
    user = request.user
    if request.method == 'POST':
        form = IrctcPassFormField(request.POST, request.FILES)
        if form.is_valid():
            pass_form=form.save(commit=False)
            pass_form.user = request.user
            pass_form.save()
            messages.success(request, 'application submitted')
            return redirect('dash')

        else:
            messages.error(request, 'Error in submitting your application')
            print(form.errors)
            return redirect('trainpassform')
    else:
        form = IrctcPassFormField(initial={'user': user})
    return render(request, 'trainpassform.html', {'form':form, 'user': user})
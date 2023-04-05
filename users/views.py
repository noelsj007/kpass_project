from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserAdminCreationForm, KsrtcPassFormField, IrctcPassFormField, TrainStPassFormField
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorator import *
from .models import *
from ksrtc.models import *
from irctc.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django import forms
from aadhaarcardscrapper import aadhaarScrapper
import cv2
from django.db.models import Sum

# Create your views here.

# @login_required(login_url='login')
def homePage(request):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    previous_day_bus_pass_to_delete = DailyBusPassView.objects.filter(today=yesterday)
    previous_day_bus_pass_to_delete.delete()
    return render(request, 'home.html')

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer', 'superadmin', 'admin'])

def dashPage(request):
    user = request.user
    pass_forms=PassForm.objects.filter(user=user).all()
    pass_form = PassForm.objects.filter(user=request.user, paid=True).last()
    subend_date = pass_form.end_date
    paid_pass_form_count = PassForm.objects.filter(user=user, paid=True).count()
    unpaid_pass_form_count = PassForm.objects.filter(user=user, paid=False).count()
    total_bus_value = PassForm.objects.aggregate(total=Sum('amount'))['total']
    total_train_value = TrainStudentPassForm.objects.aggregate(total=Sum('amount'))['total']
    paid_train_pass_form = TrainStudentPassForm.objects.filter(user=user, paid=True).count()
    unpaid_train_pass_form = TrainStudentPassForm.objects.filter(user=user, paid=False).count()
    total_pass = paid_pass_form_count+paid_train_pass_form
    total_pending_pass = unpaid_pass_form_count+unpaid_train_pass_form
    total_payment = total_bus_value+total_train_value

    context= {
        'subend_date' : subend_date,
        'paid_pass_form_count' : paid_pass_form_count,
        'unpaid_pass_form_count' : unpaid_pass_form_count,
        # 'total_amount' : total_value,
        'pass_form' : pass_form,
        'pass_forms' : pass_forms,
        'paid_train_pass_form' : paid_train_pass_form,
        'unpaid_train_pass_form' : unpaid_train_pass_form,
        'total_pass' : total_pass,
        'total_pending_pass' : total_pending_pass,
        'total_payment' : total_payment
    }
    return render(request, 'userdashboard.html', context)

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
            image = request.FILES.get('adhaar_image')
            adhaar_no = request.POST.get('adhaar_no')
            dob = request.POST.get('dob')
            dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
            formatted_dob = dob_date.strftime('%d/%m/%Y') 
            print(type(formatted_dob))
            intadhaar_no = int(adhaar_no)
            result_aadhaar, result_dob = aadhaarScrapper(image)
            # kyc_validator = aadhaarcardscrapper(request.adhaar_image)
            # print(type(result), result)
            print(type(intadhaar_no), intadhaar_no)
            print(type(formatted_dob), type(result_dob), result_dob, formatted_dob)
            if intadhaar_no == result_aadhaar and formatted_dob == result_dob:



                # Calculate the amount based on bus_rate and sub_time
                sub_time = pass_form.time_periode.sub_time
                bus_rate = pass_form.bus_rate
                amount = int((0.1 * bus_rate * sub_time)*2)
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
                return render(request, 'payment.html', {'order': order, 'amount_inr' : amount_inr, 'pass_form' : pass_form})
            
            else:
                return JsonResponse({'status' : 'Aadhaar Verification Failed'})

        else:
            messages.error(request, 'Error in submitting your application')
            print(form.errors)

    else:
        form = KsrtcPassFormField(initial={'user': user})

    return render(request, 'buspassform.html', {'form': form, 'user': user})


@csrf_exempt
def razorpay_payment(request, pass_id):
    
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
        pass_form = PassForm.objects.filter(user=request.user,id=pass_id, paid=False).first()
        verification_url = f"{request.scheme}://{request.get_host()}/{pass_form.id}/verify/"
        if pass_form is not None:
            print(f'PassForm instance found: {pass_form}')
            pass_form.paid = True
            pass_form.payment_id = payment_id
            pass_form.signature = signature
            pass_form.order_id = order_id
            pass_form.save()
            print(f'PassForm instance updated: {pass_form}')

            # Send an email to the school with the verification link
            subject = 'Verification link for pass form'
            message = f'Please verify the pass form submitted by {pass_form.name}. Click on the following link to verify:\n\n{verification_url}'
            from_email = settings.EMAIL_HOST_USER
            to_email = pass_form.school_name.school_email
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            return JsonResponse({'status': 'success'})
        else:
            print('No PassForm instance found for the current user')
            return JsonResponse({'status': 'failure', 'message': 'No unpaid pass forms found for the current user'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request method'})

def verifyBusPass(request, pass_id):
    pass_form = PassForm.objects.filter(id=pass_id).first()
    if pass_form.is_verified:
        return JsonResponse({'status': 'Already Verified'})
    else:
        print(pass_form.name)
        # pass_form = PassForm.objects.filter(user=request.user, is_verified=False).first()
        if request.method == 'POST':
            if 'confirm' in request.POST:
                pass_form.is_verified = True
                pass_form.verification_date = datetime.date.today()
                pass_form.save()
                
                print(f'PassForm instance updated: {pass_form}')
                return JsonResponse({'status': 'success'})
            elif 'cancel' in request.POST:
                return redirect('verification_cancel.html')

    return render(request, 'buspassverify.html', {'pass_form' : pass_form})

def verifyTrainPass(request, pass_id):
    pass_form = TrainStudentPassForm.objects.filter(id=pass_id).first()
    if pass_form.is_verified:
        return JsonResponse({'status': 'Already Verified'})
    else:
        print(pass_form.name)
        # pass_form = PassForm.objects.filter(user=request.user, is_verified=False).first()
        if request.method == 'POST':
            if 'confirm' in request.POST:
                pass_form.is_verified = True
                pass_form.verification_date = datetime.date.today()
                pass_form.save()
                
                print(f'PassForm instance updated: {pass_form}')
                return JsonResponse({'status': 'success'})
            elif 'cancel' in request.POST:
                return redirect('verification_cancel.html')

    return render(request, 'trainpassverify.html', {'pass_form' : pass_form})


@login_required
def view_pass_forms(request):
    user = request.user
    pass_forms = PassForm.objects.filter(user=user)
    return render(request, 'viewpassforms.html', {'pass_forms': pass_forms})


def TrainPassForm(request):


    user = request.user
    if request.method == 'POST':
        form = TrainStPassFormField(request.POST, request.FILES)
        if form.is_valid():
            pass_form = form.save(commit=False)
            pass_form.user = user
            image = request.FILES.get('adhaar_image')
            adhaar_no = request.POST.get('adhaar_no')
            dob = request.POST.get('dob')
            dob_date = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
            formatted_dob = dob_date.strftime('%d/%m/%Y') 
            print(type(formatted_dob))
            intadhaar_no = int(adhaar_no)
            result_aadhaar, result_dob = aadhaarScrapper(image)
            # kyc_validator = aadhaarcardscrapper(request.adhaar_image)
            # print(type(result), result)
            print(type(intadhaar_no), intadhaar_no)
            print(type(formatted_dob), type(result_dob), result_dob, formatted_dob)
            if intadhaar_no == result_aadhaar and formatted_dob == result_dob:



                # Calculate the amount based on bus_rate and sub_time
                sub_time = pass_form.time_periode.sub_time
                bus_rate = pass_form.train_rate
                amount = int((0.1 * bus_rate * sub_time)*2)
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
                return render(request, 'trainpayment.html', {'order': order, 'amount_inr' : amount_inr, 'pass_form' : pass_form})
            
            else:
                return JsonResponse({'status' : 'Aadhaar Verification Failed'})

        else:
            messages.error(request, 'Error in submitting your application')
            print(form.errors)

    else:
        form = TrainStPassFormField(initial={'user': user})

    return render(request, 'trainpassform.html', {'form': form, 'user': user})


@csrf_exempt
def trainst_razorpay_payment(request, pass_id):
    
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
        pass_form = TrainStudentPassForm.objects.filter(user=request.user,id=pass_id, paid=False).first()
        verification_url = f"{request.scheme}://{request.get_host()}/{pass_form.id}/train/verify/"
        if pass_form is not None:
            print(f'PassForm instance found: {pass_form}')
            pass_form.paid = True
            pass_form.payment_id = payment_id
            pass_form.signature = signature
            pass_form.order_id = order_id
            pass_form.save()
            print(f'PassForm instance updated: {pass_form}')

            # Send an email to the school with the verification link
            subject = 'Verification link for pass form'
            message = f'Please verify the pass form submitted by {pass_form.name}. Click on the following link to verify:\n\n{verification_url}'
            from_email = settings.EMAIL_HOST_USER
            to_email = pass_form.school_name.school_email
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            return JsonResponse({'status': 'success'})
        else:
            print('No PassForm instance found for the current user')
            return JsonResponse({'status': 'failure', 'message': 'No unpaid pass forms found for the current user'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request method'})


def busPassView(request):
    user = request.user
    pass_forms = PassForm.objects.filter(user=user, is_verified=True)
    return render(request, 'buspassview.html',{'pass_forms': pass_forms})

def busVirtualPassView(request, pass_id):
    user = request.user
    pass_forms = PassForm.objects.filter(id=pass_id).first()
    daily_pass = DailyBusPassView
    if pass_forms.is_verified == True:
        start_date = pass_forms.verification_date
        end_date = datetime.datetime.strptime(str(pass_forms.end_date), '%Y-%m-%d').date()
        print(end_date)
        # end_date = datetime.date(pass_forms.end_date) 
        today = datetime.datetime.now().date()
        if today <= end_date:
            daily_pass = DailyBusPassView.objects.get_or_create(today=today, end_date= end_date, pass_identity=pass_forms)
            daily_pass_object = daily_pass[0]
            print(daily_pass_object.checkbox1)
            checkbox_data = {
                'date': today,

            }
            if request.method == 'POST':
                if 'checkbox1' in request.POST:
                    daily_pass_object.checkbox1 = True
        
                if 'checkbox2' in request.POST:
                    daily_pass_object.checkbox2 = True

                daily_pass_object.save()
            return render(request, 'busvirtualpassview.html', {'pass_forms': pass_forms, 'checkbox_data': checkbox_data, 'daily_pass' : daily_pass_object})
        else:
            return JsonResponse({'Status': 'Pass Expired'})
    else:
        return JsonResponse({'status' : 'Note verified'})
    print(checkbox_data, end_date)

  # dates = []
    # current_date = start_date
    # while current_date <= end_date:
    #     dates.append(current_date)
    #     current_date += timedelta(days=1)

    # checkbox_data = []
    # for date in dates:
    #     checkbox_data.append({
    #         'date' : date,
    #         'cehckbox1' : forms.BooleanField(required=False),
    #         'checkbox2' : forms.BooleanField(required=False),
    #     })


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
previous_day_bus_pass_to_delete = DailyBusPassView.objects.filter(today=yesterday)
previous_day_bus_pass_to_delete.delete()
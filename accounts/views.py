from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

from biodata.models import Biodata
from .models import EmailConfirmed, Favourite
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.views.decorators.csrf import csrf_exempt
from biodata.models import Notification

from biodata.models import Request

# def Accounts(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         if User.objects.filter(email = email, password = password).exists():
#             print("Successfully login")
#             return render(request, 'hm.html')
#     return render(request, 'signin.html')

def Accounts(request):
    if request.method == 'POST':
        if 'gender' in request.POST and 'email' in request.POST:
            email = request.POST['email']
            gender = request.POST['gender']
            password = request.POST['password']
            if User.objects.filter(email = email).exists():
                messages.error(request, "Email already exist, Please login")
            else:
                user = User.objects.create_user(username = email, email = email, first_name = gender, password = password)
                user.is_active = False
                user.save()
                #send email
                euser = EmailConfirmed.objects.get(user = user)
                site = get_current_site(request)
                email = user.email
                email_body = render_to_string(
                    'accounts/verify.html',
                    {
                        'email': email,
                        'domain': site.domain,
                        'activation_key': euser.activation_key
                    }
                )
                send_mail(
                    subject='Email Confirmation',
                    message=email_body,
                    from_email='mdimranh.cse@gmail.com',
                    recipient_list=[email],
                    fail_silently=True
                )
                messages.success(request, "Account created successfull. We will send you link in your email for active your account. Please active your account by click the link.")
            return redirect(request.path_info)
        elif 'recover-email' in request.POST:
            if User.objects.filter(email = request.POST['recover-email']).exists():
                user = User.objects.get(email = request.POST['recover-email'])
                #send email
                euser = EmailConfirmed.objects.get(user = user)
                site = get_current_site(request)
                email = user.email
                email_body = render_to_string(
                    'accounts/recover.html',
                    {
                        'email': email,
                        'domain': site.domain,
                        'activation_key': euser.activation_key
                    }
                )
                send_mail(
                    subject='Recover Password',
                    message=email_body,
                    from_email='mdimranh.cse@gmail.com',
                    recipient_list=[email],
                    fail_silently=True
                )
                messages.success(request, "We will send you link in your email for recover your password. Please recover your password by click the link.")
                return redirect(request.path_info)
            else:
                messages.error(request, "There haven't any account with this email.")
                return redirect(request.path_info)

        elif 'email' in request.POST and 'gender' not in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(username=email, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password!')
                return redirect(request.path_info)
    else:
        return render(request, 'accounts/signin.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def email_confirm(request, activation_key):
   euser = get_object_or_404(EmailConfirmed, activation_key = activation_key)
   if euser is not None:
       print(euser.user)
       euser.email_confirmd = True
       euser.save()
       
       user1 = User.objects.get(email = euser)
       user1.is_active = True
       user1.save()
       return render(request, 'accounts/success.html')

def password_recover(request, activation_key):
    if request.method == 'POST':
        if 'password' in request.POST:
            print(f"email = {request.POST['user_email']}")
            user = User.objects.get(email = request.POST['user_email'])
            user.set_password(request.POST['password'])
            user.save()
            return redirect('/auth')
    else:
        euser = get_object_or_404(EmailConfirmed, activation_key = activation_key)
        if euser is not None:
            euser.email_confirmd = True
            euser.save()
            return render(request, 'accounts/new_pass.html', {'user_email': euser})


def Settings(request):
   user_id = request.user.id
   user = User.objects.get(id = user_id)
   seen_biodata = Biodata.objects.get(owner = request.user)
   send_request = Notification.objects.filter(sender__owner = request.user, type = 'send').count()
   get_request = Notification.objects.filter(receiver = request.user, type = 'send').count()
   accept_request = Notification.objects.filter(sender__owner = request.user, type = 'accept').count()
   cancel_request = Notification.objects.filter(sender__owner = request.user, type = 'reject').count()
   reject_request = Notification.objects.filter(receiver = request.user, type = 'reject').count()
   context = {
       'user': user,
       'seen': seen_biodata.seen.count(),
       'send': send_request,
       'get': get_request,
       'accept': accept_request,
       'cancel': cancel_request,
       'reject': reject_request
   }
   return render(request, 'accounts/settings.html', context)


@csrf_exempt
def Favourite_bio(request):
    biodata = Biodata.objects.get(id = request.POST['biodata'])
    user = User.objects.get(id = request.POST['user_id'])
    profile, favourite = Favourite.objects.get_or_create(user = user)
    if profile.favourite.filter(id = biodata.id).exists():
        profile.favourite.remove(biodata)
    else:
        profile.favourite.add(biodata)
    return HttpResponse('Success')
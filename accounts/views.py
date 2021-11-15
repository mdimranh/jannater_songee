from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

from datetime import datetime

from biodata.models import Biodata
from success.models import Post
from .models import EmailConfirmed, Favourite
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.views.decorators.csrf import csrf_exempt
from biodata.models import Notification

from biodata.models import Request

from django.db.models import Q

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


from django.utils.timezone import now
def Settings(request):
    if request.method == "POST":
        if 'success-post' in request.POST:
            post = Post(
                user = Biodata.objects.get(owner = request.user),
                tag = Biodata.objects.get(id = request.POST['partner']),
                post = request.POST['success-post']
            )
            post.save()
            return redirect(request.path_info)
        else:
            post = Post.objects.get(Q(user__owner = request.user) | Q(tag__owner = request.user))
            post.post = request.POST['update-post']
            post.updated_on = datetime.now()
            post.save()
            return redirect(request.path_info)
    
    else:
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        seen_biodata = Biodata.objects.get(owner = request.user)
        send_request_all = Notification.objects.filter(receiver = request.user, type = 'send').distinct("sender").count()
        get_request_all = Notification.objects.filter(sender__owner = request.user, type = 'send').distinct("receiver").count()
        accept_request_all = Notification.objects.filter(sender__owner = request.user, type = 'accept').distinct("receiver").count()
        cancel_request = Notification.objects.filter(Q(sender__owner = request.user) & (Q(Q(type = 'reject') | Q(type = 'cancel')))).distinct("receiver").count()
        reject_request_all = Notification.objects.filter(receiver = request.user, type = 'reject').distinct("sender").count()
        accept = Request.objects.filter(user = request.user, accept = True).count()
        reject = Notification.objects.filter(sender__owner = request.user, type = 'reject').distinct("receiver").count()
        send = Request.objects.filter(request_user = request.user).count()
        accept_all1 = Request.objects.filter(user = request.user, accept = True)
        accept_all2 = Request.objects.filter(request_user = request.user, accept = True)
        post = Post.objects.filter(Q(user__owner = request.user) | Q(tag__owner = request.user))
        context = {
            'user': user,
            'send': send,
            'accept': accept,
            'reject': reject,
            'seen': seen_biodata.seen.count(),
            'send_all': send_request_all,
            'get_all': get_request_all,
            'accept_all': accept_request_all,
            'cancel': cancel_request,
            'reject_all': reject_request_all,
            'accept_all1': accept_all1,
            'accept_all2': accept_all2,
            'post': post
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
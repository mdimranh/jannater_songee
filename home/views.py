from django import template
from django.db.models.query_utils import Q, PathInfo
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators import csrf
from accounts.models import Favourite
from biodata.models import Biodata, Notification, Request, Suggested

from django.contrib.auth.models import User
from django.template import context
from .models import Quotes

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# div = ['ঢাকা বিভাগ', 'চট্টগ্রাম বিভাগ', 'রাজশাহী বিভাগ', 'খুলনা বিভাগ', 'বরিশাল বিভাগ', 'সিলেট বিভাগ', 'রংপুর বিভাগ', 'ময়মনসিংহ বিভাগ']
dhaka = ['গাজীপুর', 'ঢাকা', 'ফরিদপুর', 'গোপালগঞ্জ', 'কিশোরগঞ্জ', 'মাদারীপুর', 'মানিকগঞ্জ', 'মুন্সিগঞ্জ', 'নারায়ণগঞ্জ', 'নরসিংদী', 'রাজবাড়ী', 'শরীয়তপুর', 'টাঙ্গাইল']
chottogram = ['বান্দরবান','ব্রাহ্মণবাড়িয়া','চাঁদপুর','চট্টগ্রাম','কুমিল্লা','কক্সবাজার','ফেনী','খাগড়াছড়ি','লক্ষ্মীপুর','নোয়াখালী','রাঙ্গামাটি']
rajshahi = ['বগুড়া','জয়পুরহাট','নওগাঁ','নাটোর','চাঁপাইনবাবগঞ্জ','পাবনা','রাজশাহী','সিরাজগঞ্জ']
khulna = ['বাগেরহাট', 'চুয়াডাঙ্গা', 'যশোর', 'ঝিনাইদহ', 'খুলনা', 'কুষ্টিয়া', 'মাগুরা', 'মেহেরপুর', 'নড়াইল', 'সাতক্ষীরা']
borisal = ['বরগুনা', 'বরিশাল', 'ভোলা', 'ঝালকাঠি', 'পটুয়াখালী', 'পিরোজপুর']
sylhet = ['হবিগঞ্জ', 'মৌলভীবাজার', 'সুনামগঞ্জ', 'সিলেট']
rangpur = ['দিনাজপুর', 'গাইবান্ধা', 'কুড়িগ্রাম', 'লালমনিরহাট', 'নীলফামারী', 'পঞ্চগড়', 'রংপুর', 'ঠাকুরগাঁও']
mymensingh = ['জামালপুর', 'ময়মনসিংহ', 'নেত্রকোণা', 'শেরপুর']
dis = [('ঢাকা বিভাগ', dhaka), ('চট্টগ্রাম বিভাগ', chottogram), ('রাজশাহী বিভাগ', rajshahi), ('খুলনা বিভাগ', khulna), ('বরিশাল বিভাগ', borisal), ('সিলেট বিভাগ', sylhet), ('রংপুর বিভাগ', rangpur), ('ময়মনসিংহ বিভাগ', mymensingh)]




def home(request):

    if request.method == 'POST':
        if 'gender' in request.POST:
            getuser = User.objects.get(id = request.user.id)
            gender = request.POST['gender']
            getuser.first_name = gender
            getuser.save()
            return redirect(request.path_info)

        if 'bio_type' in request.POST:
            bio_type = request.POST['bio_type']
            print(bio_type)
            district = request.POST.getlist('district')
            color = request.POST.getlist('color')
            edu_type = request.POST['edu_type']
            if edu_type == 'any':
                edu_type = ['জেনারেল', 'মাদ্রাসা', 'আগে মাদ্রাসা এখন জেনারেল', 'আগে জেনারেল এখন মাদ্রাসা', 'জেনারেল এবং মাদ্রাসা উভয়ই', 'লেখাপড়া করিনাই']
            elif edu_type == 'জেনারেল':
                edu_type = ['জেনারেল', 'আগে মাদ্রাসা এখন জেনারেল', 'আগে জেনারেল এখন মাদ্রাসা', 'জেনারেল এবং মাদ্রাসা উভয়ই']
            elif edu_type == 'মাদ্রাসা':
                edu_type = ['মাদ্রাসা', 'আগে মাদ্রাসা এখন জেনারেল', 'আগে জেনারেল এখন মাদ্রাসা', 'জেনারেল এবং মাদ্রাসা উভয়ই']
            age1 = request.POST['age1']
            age2 = request.POST['age2']
            height1 = request.POST['height1']
            height2 = request.POST['height2']
            if bio_type == 'all':
                biodata = Biodata.objects.filter(permanent_address__in = district, color__in = color, education_category__in = edu_type, height__gte = height1, height__lte = height2)
            else:
                biodata = Biodata.objects.filter(owner__first_name = bio_type, permanent_address__in = district, color__in = color, education_category__in = edu_type, height__gte = height1, height__lte = height2)
            context = {
                'title': 'বায়োডাটাসমূহ',
                'biodata': biodata,
                'dis': dis
            }
            return render(request, 'hm.html', context)

    quotes = Quotes.objects.all()
    context = {
        'home': True,
        'title': 'হোম',
        'quotes': quotes,
        'dis': dis
    }
    return render(request, 'hm.html', context)

def All(request):
    if request.user.is_authenticated:
        biodata = Biodata.objects.all().order_by('created_at').exclude(Q(publish = False) | Q(owner = request.user))
    else:
        biodata = Biodata.objects.all().order_by('created_at').exclude(Q(publish = False))
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "সকল বায়োডাটা"
    context = {
        'title': title,
        'dis': dis,
        'id': 'all',
        'biodata': page_obj,
    }
    print(f"Ip of user = {request.META.get('REMOTE_ADDR')}")
    return render(request, 'hm.html', context)

def Male(request):
    if request.user.is_authenticated:
        biodata = Biodata.objects.filter(owner__first_name = 'male').order_by('created_at').exclude(Q(publish = False) | Q(owner = request.user))
    else:
        biodata = Biodata.objects.filter(owner__first_name = 'male').order_by('created_at').exclude(Q(publish = False))
    
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "পাত্রর বায়োডাটাসমূহ"
    context = {
        'title': title,
        'dis': dis,
        'id': 'male',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)

def Female(request):
    if request.user.is_authenticated:
        biodata = Biodata.objects.filter(owner__first_name = 'female').order_by('created_at').exclude(Q(publish = False) | Q(owner = request.user))
    else:
        biodata = Biodata.objects.filter(owner__first_name = 'female').order_by('created_at').exclude(Q(publish = False))
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "পাত্রীর বায়োডাটাসমূহ"
    context = {
        'title': title,
        'dis': dis,
        'id': 'female',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)

def Suggest(request):
    biodata = Suggested.objects.filter(user = request.user).exclude(suggested__publish = False)
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "প্রস্তাবিত বায়োডাটাসমূহ"
    context = {
        'title': title,
        'dis': dis,
        'id': 'suggest',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)

def Send(request, id):
    biodata = Request.objects.filter(request_user = request.user)
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "প্রেরিত প্রস্তাব"
    context = {
        'title': title,
        'dis': dis,
        'id': 'send',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)

def Get(request, id):
    biodata = Request.objects.filter(user = request.user)
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "প্রাপ্ত প্রস্তাব"
    context = {
        'title': title,
        'dis': dis,
        'id': 'get',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)


def GetRequest(request, id):
    biodata = Notification.objects.filter(receiver = request.user, type = 'send').distinct("sender")
    paginator = Paginator(biodata, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "সকল প্রাপ্ত প্রস্তাব"
    context = {
        'title': title,
        'dis': dis,
        'id': 'get',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)


def SendRequest(request, id):
    biodata = Notification.objects.filter(sender__owner = request.user, type = 'send').distinct("receiver")
    paginator = Paginator(biodata, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    title = "সকল প্রেরিত প্রস্তাব"
    context = {
        'title': title,
        'dis': dis,
        'id': 'send',
        'biodata': page_obj,
    }
    return render(request, 'hm.html', context)

from django.views import View

class Love(View):
    template_name = 'hm.html'
    def get(self, request, *args, **kwargs):
        title = "পছন্দের বায়োডাটাসমূহ"
        profile, favourite = Favourite.objects.get_or_create(user = request.user)
        biodata = profile.favourite.all()
        context = {
            'title': title,
            'dis': dis,
            'id': 'love',
            'biodata': biodata
        }
        return render(request, self.template_name, context)


# def Love(request):
#     title = "পছন্দের বায়োডাটাসমূহ"
#     profile, favourite = Profile.objects.get_or_create(user = request.user)
#     biodata = profile.favourite.all()
#     context = {
#         'title': title,
#         'dis': dis,
#         'id': 'love',
#         'biodata': biodata
#     }
#     return render(request, 'hm.html', context)
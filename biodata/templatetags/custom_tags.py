from django import template
from django.db.models.expressions import F
from django.db.models import Q
from django.contrib.auth.models import User

from biodata.views import biodata
register = template.Library()
    
from biodata.models import Biodata, Notification, Notification_seen, Request
from masala.models import Hadith
  
@register.simple_tag
def has_biodata(user):
    if Biodata.objects.filter(owner = user).exists():
        return True
    else:
        return False

register.filter('has_biodata', has_biodata)

@register.simple_tag
def my_biodata_id(user):
    bio = Biodata.objects.get(owner = user)
    return bio.id 

register.filter('my_biodata_id', my_biodata_id)

@register.simple_tag
def list_to_string(lst):
    char_to_replace = {'[': '', ']': '', "'" : ''} 
    for key, value in char_to_replace.items():
        lst = lst.replace(key, value)
    gt = lst.rfind(",")
    x = 0
    text = ''
    for i in lst:
        if x == gt:
            i = ' এবং'
        text += i
        x += 1
    return text

register.filter('list_to_string', list_to_string)


@register.simple_tag
def list_to_string_home(lst, user):
    lst = lst.replace('লেখাপড়া করতেছি', 'লেখাপড়া করতেছি ('+user.education_category+')')
    char_to_replace = {'[': '', ']': '', "'" : ''} 
    for key, value in char_to_replace.items():
        lst = lst.replace(key, value)
    gt = lst.rfind(",")
    x = 0
    text = ''
    for i in lst:
        if x == gt:
            i = ' এবং'
        text += i
        x += 1
    return text
register.filter('list_to_string_home', list_to_string_home)

number = {
    '0': '০',
    '1': '১',
    '2': '২',
    '3': '৩',
    '4': '৪',
    '5': '৫',
    '6': '৬',
    '7': '৭',
    '8': '৮',
    '9': '৯',
    '.': "'"
}

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


@register.simple_tag
def eng_to_ban(value):
    vlu = ''
    for n in str(value):
        if n in num_list:
            replace = number[n]
            vlu += replace
    return vlu
register.filter('eng_bn', eng_to_ban)


dhaka = ['গাজীপুর', 'ঢাকা', 'ফরিদপুর', 'গোপালগঞ্জ', 'কিশোরগঞ্জ', 'মাদারীপুর', 'মানিকগঞ্জ', 'মুন্সিগঞ্জ', 'নারায়ণগঞ্জ', 'নরসিংদী', 'রাজবাড়ী', 'শরীয়তপুর', 'টাঙ্গাইল']
chottogram = ['বান্দরবান','ব্রাহ্মণবাড়িয়া','চাঁদপুর','চট্টগ্রাম','কুমিল্লা','কক্সবাজার','ফেনী','খাগড়াছড়ি','লক্ষ্মীপুর','নোয়াখালী','রাঙ্গামাটি']
rajshahi = ['বগুড়া','জয়পুরহাট','নওগাঁ','নাটোর','চাঁপাইনবাবগঞ্জ','পাবনা','রাজশাহী','সিরাজগঞ্জ']
khulna = ['বাগেরহাট', 'চুয়াডাঙ্গা', 'যশোর', 'ঝিনাইদহ', 'খুলনা', 'কুষ্টিয়া', 'মাগুরা', 'মেহেরপুর', 'নড়াইল', 'সাতক্ষীরা']
borisal = ['বরগুনা', 'বরিশাল', 'ভোলা', 'ঝালকাঠি', 'পটুয়াখালী', 'পিরোজপুর']
sylhet = ['হবিগঞ্জ', 'মৌলভীবাজার', 'সুনামগঞ্জ', 'সিলেট']
rangpur = ['দিনাজপুর', 'গাইবান্ধা', 'কুড়িগ্রাম', 'লালমনিরহাট', 'নীলফামারী', 'পঞ্চগড়', 'রংপুর', 'ঠাকুরগাঁও']
mymensingh = ['জামালপুর', 'ময়মনসিংহ', 'নেত্রকোণা', 'শেরপুর']

@register.simple_tag
def district(value, district):
    vlu = value[2:-2].split("', '")
    # lst = []
    # for dis in vlu:
    #     if dis in district[2:-2].split("', '"):
    #         lst.append(dis)
    return vlu
register.filter('district', district)

@register.simple_tag
def random_hadith(h):
    hd = Hadith.objects.all()
    import random
    id = random.randint(1, len(hd))
    hadith = Hadith.objects.filter(id = id)
    return hadith
register.filter('random_hadith', random_hadith)


@register.simple_tag
def notification(id):
    user = User.objects.get(id = id)
    nof = Notification.objects.filter(Q(user__id = id) | Q(biodata__owner = user))
    return nof
register.filter('notification', notification)


@register.simple_tag
def get_notification(id):
    nof = Notification.objects.filter(receiver__id = id).order_by('-created_at')
    return nof
register.filter('get_notification', get_notification)

@register.simple_tag
def no_notification(id):
    user = User.objects.get(id = id)
    seentime, create = Notification_seen.objects.get_or_create(user = user)
    nof = Notification.objects.filter(receiver__id = id, created_at__gt = seentime.seentime).count()
    return nof
register.filter('no_notification', no_notification)

@register.simple_tag
def str_to_list(value):
    return value[2:-2].split("', '")
register.filter('str_to_list', str_to_list)

@register.simple_tag
def strr(value):
    print(type(value))
    return str(value)
register.filter('strr', strr)
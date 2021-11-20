from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
from django.db.models.fields import IntegerField, TextField
from django.http import request
from ckeditor.fields import RichTextField
from datetime import datetime
from django.utils.timezone import now

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class UniqueUser(models.Model):
    ip = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.ip

class Biodata(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # general information

    name = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=50)
    present_address = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    birth_year = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    what_do = models.CharField(max_length=50)
    monthly_income = models.CharField(max_length=50, blank=True, null=True)
    job_details = models.TextField(blank=True, null=True)
    business_details = models.TextField(blank=True, null=True)
    haram_income = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.CharField(max_length=50)

    # Educational information
    
    education_category = models.CharField(max_length=100)
    ssc = models.CharField(max_length=100)
    class_no = models.CharField(max_length=50, blank=True, null=True)
    ssc_department = models.CharField(max_length=50, blank=True, null=True)
    ssc_pass_year = models.CharField(max_length=50, blank=True, null=True)
    ssc_result = models.CharField(max_length=50, blank=True, null=True)
    hsc = models.CharField(max_length=100, blank=True, null=True)
    hsc_department = models.CharField(max_length=50, blank=True, null=True)
    hsc_pass_year = models.CharField(max_length=50, blank=True, null=True)
    hsc_result = models.CharField(max_length=100, blank=True, null=True)
    graduate = models.CharField(max_length=50, blank=True, null=True)
    varsity = models.CharField(max_length=255, blank=True, null=True)
    graduate_pass_year = models.CharField(max_length=5, blank=True, null=True)
    hafez = models.CharField(max_length=50)
    para = models.CharField(max_length=50, blank=True, null=True)
    daora_hadith = models.CharField(max_length=100, blank=True, null=True)
    daora_hadith_year = models.CharField(max_length=100, blank=True, null=True)
    natiza = models.CharField(max_length=255, blank=True, null=True)
    takhassur = models.CharField(max_length=100, blank=True, null=True)
    takhassur_sub = models.CharField(max_length=255, blank=True, null=True)
    highest_education = RichTextField(blank=True, null=True)
    others_education = RichTextField(blank=True, null=True)
    why_not_education = models.TextField(blank=True, null=True)

    # Dini Information

    salat = models.CharField(max_length = 100)
    salat_duration = models.CharField(max_length = 150)
    quran_correctly = models.CharField(max_length = 150)
    quran_regularly = models.CharField(max_length = 150)
    dari = models.CharField(max_length=50, blank=True, null=True)
    shirk = models.CharField(max_length=100)
    bidat = models.CharField(max_length=100)
    aqida = models.CharField(max_length=200)
    tv = models.CharField(max_length=100)
    murid = models.CharField(max_length=100)
    majar = models.CharField(max_length=255)
    books = RichTextField()
    sheiks = RichTextField()
    dini_qualification = RichTextField(blank=True, null=True)

    # Dress Information

    pant = models.CharField(max_length=100, blank=True, null=True)
    out_dress = models.TextField(blank=True, null=True)
    borka = models.CharField(max_length=50, blank=True, null=True)
    muja = models.CharField(max_length=50, blank=True, null=True)
    mahram = models.CharField(max_length=150, blank=True, null=True)
    porda = RichTextField()

    # Family Information

    father_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    brother = models.CharField(max_length=50)
    about_brother = RichTextField()
    sister = models.CharField(max_length=50)
    about_sister = RichTextField()
    financial_status = models.CharField(max_length=255)
    social_status = models.CharField(max_length=255)
    family_haram_income = models.CharField(max_length=50)
    family_details = RichTextField()

    # Owner information

    Divorce = models.TextField(blank=True, null=True)
    children = models.CharField(max_length=50, blank=True, null=True)
    children_address = models.CharField(max_length=50, blank=True, null=True)
    weakness = models.CharField(max_length=50)
    about_weakness = models.TextField(blank=True, null=True)
    mehnot = models.CharField(max_length=100)
    about_mehnot = RichTextField(blank=True, null=True)
    about_owner = RichTextField(blank=True, null=True)

    # Marital information

    family_permission = models.CharField(max_length=150)
    education_after_married = models.CharField(max_length=250, blank=True, null=True)
    job_after_married = models.CharField(max_length=250, blank=True, null=True)
    takecare_porda = models.CharField(max_length=250, blank=True, null=True)
    study_permission= models.CharField(max_length=250, blank=True, null=True)
    job_permission = models.CharField(max_length=250, blank=True, null=True)
    address_of_wife = models.TextField(blank=True, null=True)
    joutuk = models.CharField(max_length=50)
    about_married = RichTextField()

    # Partner Information

    partner_marital_status = models.CharField(max_length=255)
    partner_age1 = models.CharField(max_length=50)
    partner_age2 = models.CharField(max_length=50)
    partner_height1 = models.CharField(max_length=50)
    partner_height2 = models.CharField(max_length=50)
    partner_color = models.CharField(max_length=255)
    partner_education = models.CharField(max_length=255)
    student_partner = models.TextField()
    partner_district = models.TextField()
    partner_aqida = models.CharField(max_length=255)
    partner_financial_status = models.TextField()
    divorced_houseband = models.CharField(max_length=255, blank=True, null=True)
    foreign_houseband = models.CharField(max_length=255, blank=True, null=True)
    bondha = models.CharField(max_length=100, blank=True, null=True)
    masna = models.CharField(max_length=255, blank=True, null=True)
    more_about_partner = RichTextField()

    # Our question

    know_family = models.CharField(max_length=50)
    right = models.CharField(max_length=50)
    wrong = models.CharField(max_length=50)

    # communication

    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()

    created_at = models.DateTimeField(default=datetime.now)
    seen = models.ManyToManyField(UniqueUser)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Suggested(models.Model):
    user = models.ForeignKey(User, related_name='user_bio', on_delete=models.CASCADE)
    suggested = models.ForeignKey(Biodata, related_name='suggested', on_delete=models.CASCADE)
    percentage = IntegerField(default=None, blank=True)

    def __str__(self):
        return self.user.email

CHOICES = (
    ("send", "send Request"),
    ("accept", "accept Request"),
    ("reject", "reject Request"),
    ("cancel", "cancel Request"),
    ("married", "married Request"),
)

class Request(models.Model):
    user = models.ForeignKey(User, related_name="get_request_user", on_delete=models.CASCADE)
    request_user = models.ForeignKey(User, related_name="requested_user", on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    action = models.CharField(max_length=50, choices=CHOICES, default='send', blank=True, null=True)

    def request_biodata(self):
        return Biodata.objects.get(owner = self.request_user)

    def user_biodata(self):
        return Biodata.objects.get(owner = self.user)

    def __str__(self):
        user_bio = Biodata.objects.get(owner = self.user)
        return user_bio.name



def time_format(timeduration):
    c = 0
    tm = ""
    for i in timeduration:
        if i != ":" and i != ",":
            tm += i
        elif i == ",":
            t = tm.split(" ")
            if int(t[0]) >= 7 and int(t[0]) < 30:
                i = int(t[0])//7
                if i == 1:
                    i = str(i)+" week ago"
                else:
                    i = str(i)+" weeks ago"
                tm = i
            elif int(t[0]) >= 31 and int(t[0]) < 366:
                i = int(t[0])//30
                if i == 1:
                    i = str(i)+" month ago"
                else:
                    i = str(i)+ " months ago"
                tm = i
            elif int(t[0]) >= 365:
                i = int(t[0])//365
                if i == 1:
                    i = str(i)+" year ago"
                else:
                    i = str(i)+ " years ago"
                tm = i
            else:
                i = " ago"
                tm += i
            break
        elif i == ":" and c == 0:
            if tm != "0":
                if tm != "1":
                    i = " hours ago"
                else:
                    i = "hour ago"
                tm += i
                c = 1
                break
            else:
                tm = ""
                c = 1
        elif i == ":" and c == 1:
            tm = int(tm)
            tm = str(tm)
            if tm == "0":
                tm = "Now"
                break
            if tm == "1":
                i = " minute ago"
                tm += i
                break
            else:
                i = " minutes ago"
                tm += i
                break
    return tm


from django.utils.timezone import now
class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(Biodata, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=CHOICES, default=None, blank=True)
    details = models.TextField(default=None, blank=True)
    created_at = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        time = time_format(str(now() - self.created_at))
        if self.receiver.first_name == 'male':
            profile = 'patri.png'
        else:
            profile = 'patro.png'
        data = {'sender': self.sender.id, 'details': self.details, 'time': time, 'profile': profile}
        async_to_sync(channel_layer.group_send)(
            'notification_%s' % self.receiver.id, {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )

        super(Notification, self).save(*args, **kwargs)

    def __str__(self):
        return self.sender.owner.email +'<-->'+ self.receiver.email

    def request_biodata(self):
        return self.sender

    def user_biodata(self):
        return Biodata.objects.get(owner = self.receiver)

from datetime import datetime
class Notification_seen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seentime = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Nitifications seen time"
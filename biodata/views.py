from datetime import datetime
from django.db.models.query_utils import PathInfo
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import resolvers
from .models import Biodata, Notification, Request, Suggested, Notification_seen, UniqueUser
from accounts.models import Favourite
from django.http import HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt


dhaka = ['গাজীপুর', 'ঢাকা', 'ফরিদপুর', 'গোপালগঞ্জ', 'কিশোরগঞ্জ', 'মাদারীপুর', 'মানিকগঞ্জ', 'মুন্সিগঞ্জ', 'নারায়ণগঞ্জ', 'নরসিংদী', 'রাজবাড়ী', 'শরীয়তপুর', 'টাঙ্গাইল']
chottogram = ['বান্দরবান','ব্রাহ্মণবাড়িয়া','চাঁদপুর','চট্টগ্রাম','কুমিল্লা','কক্সবাজার','ফেনী','খাগড়াছড়ি','লক্ষ্মীপুর','নোয়াখালী','রাঙ্গামাটি']
rajshahi = ['বগুড়া','জয়পুরহাট','নওগাঁ','নাটোর','চাঁপাইনবাবগঞ্জ','পাবনা','রাজশাহী','সিরাজগঞ্জ']
khulna = ['বাগেরহাট', 'চুয়াডাঙ্গা', 'যশোর', 'ঝিনাইদহ', 'খুলনা', 'কুষ্টিয়া', 'মাগুরা', 'মেহেরপুর', 'নড়াইল', 'সাতক্ষীরা']
borisal = ['বরগুনা', 'বরিশাল', 'ভোলা', 'ঝালকাঠি', 'পটুয়াখালী', 'পিরোজপুর']
sylhet = ['হবিগঞ্জ', 'মৌলভীবাজার', 'সুনামগঞ্জ', 'সিলেট']
rangpur = ['দিনাজপুর', 'গাইবান্ধা', 'কুড়িগ্রাম', 'লালমনিরহাট', 'নীলফামারী', 'পঞ্চগড়', 'রংপুর', 'ঠাকুরগাঁও']
mymensingh = ['জামালপুর', 'ময়মনসিংহ', 'নেত্রকোণা', 'শেরপুর']
dis = [('ঢাকা বিভাগ', dhaka), ('চট্টগ্রাম বিভাগ', chottogram), ('রাজশাহী বিভাগ', rajshahi), ('খুলনা বিভাগ', khulna), ('বরিশাল বিভাগ', borisal), ('সিলেট বিভাগ', sylhet), ('রংপুর বিভাগ', rangpur), ('ময়মনসিংহ বিভাগ', mymensingh)]


def CreateBiodata(request):

    if request.method == 'POST':
        biodata = Biodata(
            # general information
            owner = request.user,
            name = request.POST['name'],
            marital_status = request.POST['marital-status'],
            permanent_address = request.POST['permanent-address'],
            present_address = request.POST['present-address'],
            color = request.POST['color'],
            birth_year = request.POST['birth-year'],
            blood_group = request.POST['blood-group'],
            what_do = request.POST.getlist('what-do'),
            monthly_income = 0,
            job_details = request.POST['about-job'],
            business_details = request.POST['about-business'],
            haram_income = request.POST['haram_income'],
            height = request.POST['height'],
            weight = request.POST['weight'],
            # educational qualification
            education_category = request.POST['education_type'],
            ssc = request.POST['ssc'],
            class_no = request.POST['class'],
            ssc_department = request.POST['ssc-department'],
            ssc_pass_year = request.POST['sscyear'],
            ssc_result = request.POST['sscresult'],
            hsc = request.POST['hsc'],
            hsc_department = request.POST['hsc-department'],
            hsc_pass_year = request.POST['hscyear'],
            hsc_result = request.POST['hscresult'],
            graduate = request.POST['graduate'],
            varsity = request.POST['university'],
            graduate_pass_year = request.POST['graduateyear'],
            hafez = request.POST['hafez'],
            para = 0,
            daora_hadith = request.POST['daora-hadith'],
            daora_hadith_year = request.POST['daora-hadith-year'],
            natiza = request.POST['natiza'],
            takhassur = request.POST['takhassur'],
            takhassur_sub = request.POST['takhacchor_sub'],
            highest_education = request.POST['highest_education'],
            others_education = request.POST['others-education'],
            why_not_education = request.POST['not_education'],
            # dini information
            salat = request.POST['salat'],
            salat_duration = request.POST['salat_duration'],
            quran_correctly = request.POST['quran_correctly'],
            quran_regularly = request.POST['quran_regularly'],
            dari = request.POST.get('dari', False),
            shirk = request.POST['shirk'],
            bidat = request.POST['bidat'],
            aqida = request.POST['aqida'],
            tv = request.POST['tv'],
            murid = request.POST['murid'],
            majar = request.POST['majar'],
            books = request.POST.get('book'),
            sheiks = request.POST['alem'],
            dini_qualification = request.POST['dini-qualification'],
            # dress information
            pant = request.POST.get('taknu', False),
            out_dress = request.POST.get('out_dress', False),
            borka = request.POST.get('niqab', False),
            muja = request.POST.get('muja', False),
            mahram = request.POST.get('mahram', False),
            porda = request.POST.get('porda', False),
            # family information
            father_name = request.POST['fathers_name'],
            father_occupation = request.POST['fathers_occupation'],
            mother_occupation = request.POST['mothers_occupation'],
            brother = request.POST['brother'],
            about_brother = request.POST['brother_info'],
            sister = request.POST['sister'],
            about_sister = request.POST['sister_info'],
            financial_status = request.POST['family_financial_status'],
            social_status = request.POST['family_social_status'],
            family_haram_income = request.POST['family_haram_income'],
            family_details = request.POST['family_details'],
            # personal information
            Divorce = request.POST['why_divorced'],
            children = request.POST['children'],
            children_address = request.POST.get('children_address', False),
            weakness = request.POST['weakness'],
            about_weakness = request.POST['about_weakness'],
            mehnot = request.POST['mehnot'],
            about_mehnot = request.POST['about_mehnot'],
            about_owner = request.POST['aboutme'],
            # marriage information
            family_permission = request.POST['family_permission'],
            education_after_married = request.POST.get('stydy_after_marriage', False),
            job_after_married = request.POST.get('job_after_marriage', False),
            takecare_porda = request.POST.get('takecare_porda', False),
            study_permission = request.POST.get('study_permission', False),
            job_permission = request.POST.get('job_permission', False),
            address_of_wife = request.POST.get('wife_address', False),
            joutuk = request.POST.get('joutuk', False),
            about_married = request.POST['about_married'],
            # partner information
            partner_marital_status = request.POST['partner-marital-status'],
            partner_age1 = request.POST['age1'],
            partner_age2 = request.POST['age2'],
            partner_color = request.POST.getlist('partner_color'),
            partner_height1 = request.POST['height1'],
            partner_height2 = request.POST['height2'],
            partner_education = request.POST['partner_education'],
            student_partner = request.POST.get('student_partner', False),
            partner_district = request.POST.getlist('partner_district'),
            partner_aqida = request.POST.getlist('partner_aqida'),
            partner_financial_status = request.POST['partner_financial_status'],
            divorced_houseband = request.POST.get('divorced_partner', False),
            foreign_houseband = request.POST.get('foreign_partner', False),
            bondha = request.POST['bondha'],
            masna = request.POST.get('married_partner', False),
            more_about_partner = request.POST['partner_more_info'],
            # authority Question
            know_family = request.POST['parents_permission'],
            right = request.POST['swear_to_allah'],
            wrong = request.POST['swear_to_allah1'],
            # communication
            phone = request.POST['number'],
            email = request.POST['email'],
            address = request.POST['address'],
            publish = True
        )
        biodata.save()
        biodata = Biodata.objects.filter(owner = request.user)
        profile = Favourite.objects.filter(user = request.user)
        try:
            return render(request, 'biodata/biodata.html', {'biodata': biodata, 'profile': profile})
        finally:
            import datetime
            year = datetime.datetime.today().strftime("%Y")
            biodata = Biodata.objects.get(owner = request.user)
            all_biodata = Biodata.objects.all().exclude(owner__first_name = request.user.first_name)
            mark = 0
            for bio in all_biodata:
                if bio.partner_marital_status == biodata.marital_status:
                    mark+=1
                else:
                    mark+=0
                age = int(year) - int(biodata.birth_year)
                if int(bio.partner_age1) >= age and int(bio.partner_age2) <= age:
                    mark+=1
                else:
                    mark+=0
                if bio.partner_color == biodata.color:
                    mark+=1
                else:
                    mark+=0
                # if bio.partner_marital_status == biodata.marital_status:
                #     mark+=1
                # else:
                #     mark+=0
                # if bio.partner_marital_status == biodata.marital_status:
                #     mark+=1
                # else:
                #     mark+=0
                # if bio.partner_marital_status == biodata.marital_status:
                #     mark+=1
                # else:
                #     mark+=0
                if bio.partner_aqida == biodata.aqida:
                    mark+=1
                else:
                    mark+=0
                if bio.partner_financial_status == biodata.financial_status:
                    mark+=1
                else:
                    mark+=0
                suggested = Suggested(
                    user = bio.owner,
                    suggested = biodata,
                    percentage = mark
                )
                suggested.save()

    else:    
        if Biodata.objects.filter(owner = request.user).exists():
            return render(request, 'hm.html', {"dis": dis})
        else:
            return render(request, 'biodata/create_biodata.html', {"dis": dis})


from django.db.models import Q
def biodata(request, id):
    if request.method == 'POST':
        if 'send_request' in request.POST:
            biodata = Biodata.objects.get(id = request.POST['biodata'])
            if Request.objects.filter((Q(request_user = request.user) & Q(user = biodata.owner)) | (Q(user = request.user) & Q(request_user = biodata.owner))).exists():
                rqst = Request.objects.filter((Q(request_user = request.user) & Q(user = biodata.owner)) | (Q(user = request.user) & Q(request_user = biodata.owner)))
                for rq in rqst:
                    rq.user = biodata.owner
                    rq.request_user = request.user
                    rq.action = 'send'
                    rq.seen = False
                    rq.save()
            else:
                rqst = Request(
                    user = biodata.owner,
                    request_user = request.user
                )
                rqst.save()
            # biodata = Biodata.objects.get(id = request.POST['biodata'])
            # profile = Favourite.objects.filter(user = request.user)
            # rqst = Request.objects.filter(user = biodata.owner, request_user = request.user)
            try:
                return redirect(request.path_info)
            finally:
                notification = Notification(
                    sender = Biodata.objects.get(owner = request.user),
                    receiver = biodata.owner,
                    type = 'send',
                    details = 'আপনাকে প্রস্তাব পাঠিয়েছে'
                )
                notification.save()
        elif 'cancel_request' in request.POST:
            biodata = Biodata.objects.get(id = request.POST['biodata'])
            rqst = Request.objects.get(request_user = request.user, user = biodata.owner)
            rqst.action = 'cancel'
            rqst.save()
            # biodata = Biodata.objects.get(id = request.POST['biodata'])
            # profile = Favourite.objects.filter(user = request.user)
            # rqst = Request.objects.filter(user = biodata.owner, request_user = request.user)
            try:
                return redirect(request.path_info)
            finally:
                notification = Notification(
                    sender = Biodata.objects.get(owner = request.user),
                    receiver = biodata.owner,
                    type = 'cancel',
                    details = 'তার প্রস্তাব বাতিল করেছে'
                )
                notification.save()
        elif 'accept_request' in request.POST:
            biodata = Biodata.objects.get(id = request.POST['biodata'])
            rqst = Request.objects.get(user = request.user, request_user = biodata.owner)
            rqst.action = 'accept'
            rqst.save()
            # biodata = Biodata.objects.get(id = request.POST['biodata'])
            # profile = Favourite.objects.filter(user = request.user)
            # rqst = Request.objects.filter(user = request.user, request_user = biodata.owner)
            try:
                return redirect(request.path_info)
            finally:
                notification = Notification(
                    sender = Biodata.objects.get(owner = request.user),
                    receiver = biodata.owner,
                    type = 'accept',
                    details = 'আপনার প্রস্তাব গ্রহণ করেছে'
                )
                notification.save()
        elif 'reject_request' in request.POST:
            biodata = Biodata.objects.get(id = request.POST['biodata'])
            rqst = Request.objects.get(user = request.user, request_user = biodata.owner)
            rqst.action = 'reject'
            rqst.save()
            # biodata = Biodata.objects.get(id = request.POST['biodata'])
            # profile = Favourite.objects.filter(user = request.user)
            # rqst = Request.objects.filter(user = request.user, request_user = biodata.owner)
            try:
                return redirect(request.path_info)
            finally:
                notification = Notification(
                    sender = Biodata.objects.get(owner = request.user),
                    receiver = biodata.owner,
                    type = 'reject',
                    details = 'আপনার প্রস্তাব প্রত্যাখ্যান করেছে'
                )
                notification.save()

    else:
        biodata = Biodata.objects.get(id = id)
        district = biodata.partner_district
        st = district[2:-2]
        ds = st.split("', '")
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        get, add = UniqueUser.objects.get_or_create(ip = ip)

        if get not in biodata.seen.all():
            biodata.seen.add(get)

        if request.user.is_authenticated:
            profile = Favourite.objects.filter(user = request.user)
            if Request.objects.filter(user = biodata.owner, request_user = request.user).exists():
                rqst = Request.objects.get(user = biodata.owner, request_user = request.user)
                rqst.seen = True
                rqst.save()
            if Request.objects.filter(user = biodata.owner, request_user = request.user).exists():
                rqst = Request.objects.filter(user = biodata.owner, request_user = request.user)
            else:
                rqst = Request.objects.filter(user = request.user, request_user = biodata.owner)
            return render(request, 'biodata/biodata.html', {'bio': biodata, 'profile': profile, 'request': rqst, 'dis': dis, 'district': ds})
        else:
            return render(request, 'biodata/biodata.html', {'bio': biodata, 'dis': dis, 'district': ds})


def EditBiodata(request, id):
    if request.method == 'POST':
        print(f"Birth year = {request.POST['birth-year']}")
        biodata = Biodata.objects.get(owner = request.user)
        # general information
        biodata.name = request.POST['name']
        biodata.marital_status = request.POST['marital-status']
        biodata.permanent_address = request.POST['permanent-address']
        biodata.present_address = request.POST['present-address']
        biodata.color = request.POST['color']
        biodata.birth_year = request.POST['birth-year']
        biodata.blood_group = request.POST['blood-group']
        biodata.what_do = request.POST.getlist('what-do')
        biodata.monthly_income = request.POST['monthly-income']
        biodata.job_details = request.POST['about-job']
        biodata.business_details = request.POST['about-business']
        biodata.haram_income = request.POST['haram_income']
        biodata.height = request.POST['height']
        biodata.weight = request.POST['weight']
        # educational qualification
        biodata.education_category = request.POST['education_type']
        if request.POST['education_type'] == 'লেখাপড়া করিনাই':
            biodata.ssc = None
            biodata.class_no = None
            biodata.ssc_department = None
            biodata.ssc_pass_year = None
            biodata.ssc_result = None
            biodata.hsc = None
            biodata.hsc_department = None
            biodata.hsc_pass_year = None
            biodata.hsc_result = None
            biodata.graduate = None
            biodata.varsity = None
            biodata.graduate_pass_year = None
            biodata.daora_hadith = None
            biodata.daora_hadith_year = None
            biodata.natiza = None
            biodata.takhassur = None
            biodata.takhassur_sub = None
            biodata.highest_education = None
            biodata.others_education = None
            biodata.why_not_education = request.POST['not_education']
        elif request.POST['education_type'] == 'জেনারেল':
            biodata.ssc = request.POST['ssc']
            biodata.ssc_department = request.POST['ssc-department']
            biodata.ssc_pass_year = request.POST['sscyear']
            biodata.ssc_result = request.POST['sscresult']
            if request.POST['ssc'] == 'না' or request.POST['ssc'] == 'পড়তেছি':
                biodata.class_no = None
                biodata.hsc = None
                biodata.hsc_department = None
                biodata.hsc_pass_year = None
                biodata.hsc_result = None
                biodata.graduate = None
                biodata.varsity = None
                biodata.graduate_pass_year = None
            elif request.POST['ssc'] == 'হ্যাঁ':
                biodata.class_no = request.POST['class']
                biodata.hsc = request.POST['hsc']
                biodata.hsc_department = request.POST['hsc-department']
                biodata.hsc_pass_year = request.POST['hscyear']
                biodata.hsc_result = request.POST['hscresult']
                if request.POST['hsc'] == 'না' or request.POST['hsc'] == 'পড়তেছি':
                    biodata.graduate = None
                    biodata.varsity = None
                    biodata.graduate_pass_year = None
                elif request.POST['hsc'] == 'হ্যাঁ':
                    biodata.graduate = request.POST['graduate']
                    biodata.varsity = request.POST['university']
                    if request.POST['graduate'] == 'না পড়িনাই' or request.POST['graduate'] == 'পড়ব ইনশাআল্লাহ' or request.POST['graduate'] == 'হ্যাঁ পড়তেছি':
                        biodata.graduate_pass_year = None
                    elif request.POST['graduate'] == "হ্যাঁ পড়েছি":
                        biodata.graduate_pass_year = request.POST['graduateyear']
            biodata.daora_hadith = None
            biodata.daora_hadith_year = None
            biodata.natiza = None
            biodata.takhassur = None
            biodata.takhassur_sub = None
            biodata.highest_education = request.POST['highest_education']
            biodata.others_education = request.POST['others-education']
            biodata.why_not_education = None
        elif request.POST['education_type'] != 'জেনারেল' and request.POST['education_type'] != 'লেখাপড়া করিনাই':
            biodata.ssc = request.POST['ssc']
            biodata.class_no = request.POST['class']
            biodata.ssc_department = request.POST['ssc-department']
            biodata.ssc_pass_year = request.POST['sscyear']
            biodata.ssc_result = request.POST['sscresult']
            biodata.hsc = request.POST['hsc']
            biodata.hsc_department = request.POST['hsc-department']
            biodata.hsc_pass_year = request.POST['hscyear']
            biodata.hsc_result = request.POST['hscresult']
            biodata.graduate = request.POST['graduate']
            biodata.varsity = request.POST['university']
            biodata.graduate_pass_year = request.POST['graduateyear']
            biodata.daora_hadith = request.POST['daora-hadith']
            biodata.daora_hadith_year = request.POST['daora-hadith-year']
            biodata.natiza = request.POST['natiza']
            biodata.takhassur = request.POST['takhassur']
            biodata.takhassur_sub = request.POST['takhacchor_sub']
            biodata.highest_education = request.POST['highest_education']
            biodata.others_education = request.POST['others-education']
            biodata.why_not_education = None
        biodata.hafez = request.POST['hafez']
        biodata.para = request.POST['para']
        # dini information
        biodata.salat = request.POST['salat']
        biodata.salat_duration = request.POST['salat_duration']
        biodata.quran_correctly = request.POST['quran_correctly']
        biodata.quran_regularly = request.POST['quran_regularly']
        biodata.dari = request.POST.get('dari', False)
        biodata.shirk = request.POST['shirk']
        biodata.bidat = request.POST['bidat']
        biodata.aqida = request.POST['aqida']
        biodata.tv = request.POST['tv']
        biodata.murid = request.POST['murid']
        biodata.majar = request.POST['majar']
        biodata.books = request.POST.get('book')
        biodata.sheiks = request.POST['alem']
        biodata.dini_qualification = request.POST['dini-qualification']
        # dress information
        biodata.pant = request.POST.get('taknu', False)
        biodata.out_dress = request.POST.get('out_dress', False)
        biodata.borka = request.POST.get('niqab', False)
        biodata.muja = request.POST.get('muja', False)
        biodata.mahram = request.POST.get('mahram', False)
        biodata.porda = request.POST.get('porda', False)
        # family information
        biodata.father_name = request.POST['fathers_name']
        biodata.father_occupation = request.POST['fathers_occupation']
        biodata.mother_occupation = request.POST['mothers_occupation']
        biodata.brother = request.POST['brother']
        biodata.about_brother = request.POST['brother_info']
        biodata.sister = request.POST['sister']
        biodata.about_sister = request.POST['sister_info']
        biodata.financial_status = request.POST['family_financial_status']
        biodata.social_status = request.POST['family_social_status']
        biodata.family_haram_income = request.POST['family_haram_income']
        biodata.family_details = request.POST['family_details']
        # personal information
        biodata.Divorce = request.POST['why_divorced']
        biodata.children = request.POST['children']
        biodata.children_address = request.POST.get('children_address', False)
        biodata.weakness = request.POST['weakness']
        biodata.about_weakness = request.POST['about_weakness']
        biodata.mehnot = request.POST['mehnot']
        biodata.about_mehnot = request.POST['about_mehnot']
        biodata.about_owner = request.POST['aboutme']
        # marriage information
        biodata.family_permission = request.POST['family_permission']
        biodata.education_after_married = request.POST.get('stydy_after_marriage', False)
        biodata.job_after_married = request.POST.get('job_after_marriage', False)
        biodata.takecare_porda = request.POST.get('takecare_porda', False)
        biodata.study_permission = request.POST.get('study_permission', False)
        biodata.job_permission = request.POST.get('job_permission', False)
        biodata.address_of_wife = request.POST.get('wife_address', False)
        biodata.joutuk = request.POST.get('joutuk', False)
        biodata.about_married = request.POST['about_married']
        # partner information
        biodata.partner_marital_status = request.POST.getlist('partner-marital-status')
        biodata.partner_age1 = request.POST['age1']
        biodata.partner_age2 = request.POST['age2']
        biodata.partner_color = request.POST.getlist('partner_color')
        biodata.partner_height1 = request.POST['height1']
        biodata.partner_height2 = request.POST['height2']
        biodata.partner_education = request.POST['partner_education']
        biodata.student_partner = request.POST.get('student_partner', False)
        biodata.partner_district = request.POST.getlist('partner_district')
        biodata.partner_aqida = request.POST.getlist('partner_aqida')
        biodata.partner_financial_status = request.POST.getlist('partner_financial_status')
        biodata.divorced_houseband = request.POST.get('divorced_partner', False)
        biodata.foreign_houseband = request.POST.get('foreign_partner', False)
        biodata.bondha = request.POST['bondha']
        biodata.masna = request.POST.get('married_partner', False)
        biodata.more_about_partner = request.POST['partner_more_info']
        # authority Question
        biodata.know_family = request.POST['parents_permission']
        biodata.right = request.POST['swear_to_allah']
        biodata.wrong = request.POST['swear_to_allah1']
        # communication
        biodata.phone = request.POST['number']
        biodata.email = request.POST['email']
        biodata.address = request.POST['address']
        biodata.save()
        try:
            return redirect(request.path_info)
        finally:
            import datetime
            year = datetime.datetime.today().strftime("%Y")
            biodata = Biodata.objects.get(owner = request.user)
            Suggested.objects.filter(Q(suggested = biodata) | Q(user = biodata.owner)).delete()
            all_biodata = Biodata.objects.all().exclude(owner__first_name = request.user.first_name)
            mark = 0
            for bio in all_biodata:
                if bio.marital_status in biodata.partner_marital_status[2:-2].split("', '"):
                    mark+=1
                    print("partner_marital_status")
                age = int(year) - int(biodata.birth_year)
                if age >= int(biodata.partner_age1) and age <= int(biodata.partner_age2):
                    mark+=1
                    print("partner_age")
                if biodata.color in biodata.partner_color[2:-2].split("', '"):
                    mark+=1
                    print("partner_color")
                if bio.height >= int(biodata.partner_height1)*12 and bio.height <= int(biodata.partner_height2)*12:
                    mark+=1
                    print("partner_height")
                if bio.aqida in biodata.partner_aqida[2:-2].split("', '"):
                    mark+=1
                    print("partner_aqida")
                if biodata.financial_status in bio.partner_financial_status[2:-2].split("', '"):
                    mark+=1
                    print("financial_status")
                suggested = Suggested(
                    user = bio.owner,
                    suggested = biodata,
                    percentage = mark
                )
                suggested.save()

    else:
        if request.user.is_authenticated:
            if Biodata.objects.filter(owner = request.user).exists():
                biodata = Biodata.objects.filter(owner = request.user)
                bio = Biodata.objects.get(owner = request.user)
            else:
                return redirect('/')
            district = bio.partner_district
            st = district[2:-2]
            ds = st.split("', '")
            return render(request, 'biodata/edit_biodata.html', {'biodata': biodata, 'dis': dis, 'district': ds})
        else:
            if Biodata.objects.filter(id = id).exists():
                bio = Biodata.objects.get(id = id)
                return render(request, 'biodata/biodata.html', {'bio': bio})
            else:
                return redirect("/")






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

def Notifications(request):
    if request.user.id is not None:
        seen = Notification_seen.objects.get(user = request.user.id)
        no_notification = Notification.objects.filter(receiver__id = request.user.id, created_at__gt = seen.seentime).order_by('-created_at').count()
        nof = Notification.objects.filter(receiver__id = request.user.id).order_by('-created_at')
        timelist = []
        userlist = []
        for x in nof:
            timeduration = str(now() - x.created_at)
            timelist.append(time_format(timeduration))
            userlist.append(x.sender.id)
        if request.user.first_name == 'male':
            profile = 'patri.png'
        else:
            profile = 'patro.png'
        context = {
            'notification': list(nof.values()),
            'no_all': nof.count(),
            'no_notification': no_notification,
            'timelist': timelist,
            'userlist': userlist,
            'profile': profile,
            'gender': request.user.first_name
        }
        return JsonResponse(context)
    else:
        context = {}
        return JsonResponse(context)

@csrf_exempt
def notifications_seen(request):
    user = User.objects.get(id = request.POST['id'])
    get, create = Notification_seen.objects.get_or_create(user = user)
    get.seentime = datetime.now()
    get.save()
    return HttpResponse('Success')
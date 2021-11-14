from django.shortcuts import render
from .models import masala, masala_catagory

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Masala(request):
    msla = masala.objects.all()
    paginator = Paginator(msla, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'masala/masala.html', {'masala':page_obj, 'id': "masala"})

def MasalaCat(request, title):
    cat = masala_catagory.objects.get(title = title)
    msla = masala.objects.filter(catagory = cat)
    paginator = Paginator(msla, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'masala': page_obj,
        'cat': cat,
        'id': "masala"
    }
    return render(request, 'masala/masala.html', context)

def GetMasala(request, id):
    msla = masala.objects.filter(id = id)
    msla1 = masala.objects.get(id = id)
    related_masala = masala.objects.filter(catagory = msla1.catagory).exclude(id = id)
    extra_related_masala = masala.objects.all().exclude(catagory = msla1.catagory)
    return render(request, 'masala/masla-details.html', {'masala': msla, 'rmasala': related_masala, 'exmasala': extra_related_masala, 'id': "masala"})

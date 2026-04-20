from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages

from .models import Talaba, Guruh
from .forms import TalabaForm, GuruhForm

from django.shortcuts import render
from .models import Talaba, Guruh

# -------------------------
# TALABALAR
# -------------------------

def talabalar_royxati(request):
    query = request.GET.get('q', '')
    guruh_id = request.GET.get('guruh', '')

    talabalar = Talaba.objects.all()

    if query:
        talabalar = talabalar.filter(
            Q(ism__icontains=query) |
            Q(familiya__icontains=query) |
            Q(email__icontains=query)
        )
    if guruh_id:
              talabalar = talabalar.filter(guruh_id=guruh_id)

    guruhlar = Guruh.objects.all()

    return render(request, 'main/royxat.html', {
        'talabalar': talabalar,
        'guruhlar': guruhlar,
        'query': query
    })


def talaba_qoshish(request):
    if request.method == 'POST':
        form = TalabaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Talaba qo‘shildi!")
            return redirect('main:list')
    else:
        form = TalabaForm()
    return render(request, 'main/forma.html', {'form': form})


def talaba_tahrirlash(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)
    if request.method == 'POST':
        form = TalabaForm(request.POST, instance=talaba)
        if form.is_valid():
            form.save()
            messages.success(request, "Talaba yangilandi!")
            return redirect('main:list')
    else:
        form = TalabaForm(instance=talaba)

    return render(request, 'main/forma.html', {'form': form})
def talaba_detail(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)
    return render(request, 'main/detail.html', {'talaba': talaba})


def talaba_ochirish(request, pk):
    talaba = get_object_or_404(Talaba, pk=pk)
    if request.method == 'POST':
        talaba.delete()
        messages.success(request, "Talaba o‘chirildi!")
        return redirect('main:list')

    return render(request, 'main/ochirish.html', {'talaba': talaba})

def guruhlar_royxati(request):
    guruhlar = Guruh.objects.all()
    return render(request, 'main/guruhlar.html', {'guruhlar': guruhlar})


def guruh_qoshish(request):
    form = GuruhForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('main:guruhlar')

    return render(request, 'main/guruh_forma.html', {'form': form})

def guruh_tahrirlash(request, pk):
    guruh = get_object_or_404(Guruh, pk=pk)
    if request.method == 'POST':
        form = GuruhForm(request.POST, instance=guruh)
        if form.is_valid():
            form.save()
            messages.success(request, "Guruh yangilandi!")
            return redirect('main:guruhlar')
    else:
        form = GuruhForm(instance=guruh)

    return render(request, 'main/guruh_forma.html', {'form': form})

def guruh_ochirish(request, pk):
    guruh = get_object_or_404(Guruh, pk=pk)
    if request.method == 'POST':
        guruh.delete()
        messages.success(request, "Guruh o‘chirildi!")
        return redirect('main:guruhlar')

    return render(request, 'main/guruh_ochirish.html', {'guruh': guruh})


def asosiy(request):
    return render(request, 'main/asosiy.html', {
        'talabalar_soni': Talaba.objects.count(),
        'guruhlar_soni': Guruh.objects.count(),
        'guruhlar': Guruh.objects.all(),
    })
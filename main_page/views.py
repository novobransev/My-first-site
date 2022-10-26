from django.shortcuts import render
from .models import InfoImg, Homework, DateNow, Title_odd_week, Title_eveen_week, Border_odd_week, Border_even_week, Desc

def home(request):
    img = InfoImg.objects.all()
    desc = Desc.objects.all()
    return render(request, 'main_page/home.html', {'content': img, 'title': 'Главная', 'desc': desc})

def schedule(request):
    neonshadow_chet = Title_eveen_week.objects.all()
    neonshadow_nechet = Title_odd_week.objects.all()
    photo_chet = Border_even_week.objects.all()
    photo_nechet = Border_odd_week.objects.all()
    return render(request, 'main_page/schedule.html', {'title': 'Расписание', 'neonshadow_chet': neonshadow_chet, 'neonshadow_nechet': neonshadow_nechet, 'photo_chet': photo_chet, 'photo_nechet': photo_nechet})

def abstract(request):
    return render(request, 'main_page/abstract.html', {'title': 'Конспекты'})

def about(request):
    return render(request, 'main_page/about.html', {'title': 'О сайте'})

def homework(request):
    dz = Homework.objects.all()
    dat = DateNow.objects.all()

    info = {'title': 'Домашняя работа', 'dz': dz, }

    if dat:
        data = dat[len(dat)-1]
        info.setdefault('data', data)

    return render(request, 'main_page/homework.html', info)

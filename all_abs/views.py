from django.shortcuts import render
from .models import Biology
from .models import Chemistry
from .models import English
from .models import History
from .models import Information
from .models import Literature
from .models import Math
from .models import OID
from .models import OBZ
from .models import Physics
from .models import Russian_language
from .models import Social_studies


def biology(request):
    abs_biology = Biology.objects.all()

    col = []
    count = 0
    for biology in abs_biology:
        if biology:
            col.append(count)
            count += 1

    info = {'abs_biology': abs_biology, 'count': count, 'col': col}

    if abs_biology:
        one = abs_biology[0]
        all = abs_biology[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/biology.html', info)



def chemistry(request):
    abs_chemistry = Chemistry.objects.all()

    col = []
    count = 0
    for chemistry in abs_chemistry:
        if chemistry:
            col.append(count)
            count += 1

    info = {'abs_chemistry': abs_chemistry, 'count': count, 'col': col}

    if abs_chemistry:
        one = abs_chemistry[0]
        all = abs_chemistry[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/chemistry.html', info)



def english(request):
    abs_english = English.objects.all()

    col = []
    count = 0
    for english in abs_english:
        if english:
            col.append(count)
            count += 1

    info = {'abs_english': abs_english, 'count': count, 'col': col}

    if abs_english:
        one = abs_english[0]
        all = abs_english[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/english.html', info)



def history(request):
    abs_history = History.objects.all()

    col = []
    count = 0
    for history in abs_history:
        if history:
            col.append(count)
            count += 1

    info = {'abs_history': abs_history, 'count': count, 'col': col}

    if abs_history:
        one = abs_history[0]
        all = abs_history[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/history.html', info)



def information(request):
    abs_information = Information.objects.all()

    col = []
    count = 0
    for information in abs_information:
        if information:
            col.append(count)
            count += 1

    info = {'abs_information': abs_information, 'count': count, 'col': col}

    if abs_information:
        one = abs_information[0]
        all = abs_information[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/information.html', info)



def literature(request):
    abs_literature = Literature.objects.all()

    col = []
    count = 0
    for literature in abs_literature:
        if literature:
            col.append(count)
            count += 1

    info = {'abs_literature': abs_literature, 'count': count, 'col': col}

    if abs_literature:
        one = abs_literature[0]
        all = abs_literature[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/literature.html', info)



def math(request):
    abs_math = Math.objects.all()

    col = []
    count = 0
    for math in abs_math:
        if math:
            col.append(count)
            count += 1


    info = {'abs_math': abs_math, 'count': count, 'col': col}

    if abs_math:
        one = abs_math[0]
        all = abs_math[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/math.html', info)



def obz(request):
    abs_obz = OBZ.objects.all()

    col = []
    count = 0
    for obz in abs_obz:
        if obz:
            col.append(count)
            count += 1

    info = {'abs_obz': abs_obz, 'count': count, 'col': col}

    if abs_obz:
        one = abs_obz[0]
        all = abs_obz[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/OBZ.html', info)



def oid(request):
    abs_oid = OID.objects.all()

    col = []
    count = 0
    for oid in abs_oid:
        if oid:
            col.append(count)
            count += 1

    info = {'abs_oid': abs_oid, 'count': count, 'col': col}

    if abs_oid:
        one = abs_oid[0]
        all = abs_oid[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/OID.html', info)



def physics(request):
    abs_physics = Physics.objects.all()

    col = []
    count = 0
    for physics in abs_physics:
        if physics:
            col.append(count)
            count += 1

    info = {'abs_physics': abs_physics, 'count': count, 'col': col}

    if abs_physics:
        one = abs_physics[0]
        all = abs_physics[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/physics.html', info)



def russian_language(request):
    abs_russian_language = Russian_language.objects.all()

    col = []
    count = 0
    for russian_language in abs_russian_language:
        if russian_language:
            col.append(count)
            count += 1

    info = {'abs_russian_language': abs_russian_language, 'count': count, 'col': col}

    if abs_russian_language:
        one = abs_russian_language[0]
        all = abs_russian_language[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)


    return render(request, 'all_abs/russian_language.html', info)



def social_studies(request):
    abs_social_studies = Social_studies.objects.all()

    col = []
    count = 0
    for social_studies in abs_social_studies:
        if social_studies:
            col.append(count)
            count += 1

    info = {'abs_social_studies': abs_social_studies, 'count': count, 'col': col}

    if abs_social_studies:
        one = abs_social_studies[0]
        all = abs_social_studies[1:]
        info.setdefault('one', one)
        info.setdefault('all', all)

    return render(request, 'all_abs/social_studies.html', info)

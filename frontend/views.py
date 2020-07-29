from django.shortcuts import render, get_object_or_404

from messier_objects.models import MessierObject
from solar_system_objects.models import SolarSystemObject


def index(request):
    return render(request, 'index.html')


def mes_obj_overview(request):

    if request.method == 'POST':
        if 'captured_only_button' in request.POST:
            list_of_mes_obj = MessierObject.objects.filter(captured=True)
        if 'not_captured_only_button' in request.POST:
            list_of_mes_obj = MessierObject.objects.filter(captured=False)
        if 'reset_filters_button' in request.POST:
            list_of_mes_obj = MessierObject.objects.all()
    else:
        list_of_mes_obj = MessierObject.objects.all()

    context = {
        "list_of_mes_obj": list_of_mes_obj
    }

    return render(request, 'api_frontends/messier_objects_overview.html', context)


def mes_obj_detail(request, mes_num):
    mes_obj = get_object_or_404(MessierObject, messier_number=mes_num)

    context = {
        "mes_obj": mes_obj
    }

    return render(request, 'api_frontends/messier_object_detail.html', context)


def sol_obj_overview(request):

    if request.method == 'POST':
        if 'captured_only_button' in request.POST:
            list_of_sol_obj = SolarSystemObject.objects.filter(captured=True)
        if 'not_captured_only_button' in request.POST:
            list_of_sol_obj = SolarSystemObject.objects.filter(captured=False)
        if 'reset_filters_button' in request.POST:
            list_of_sol_obj = SolarSystemObject.objects.all()
    else:
        list_of_sol_obj = SolarSystemObject.objects.all()

    context = {
        "list_of_sol_obj": list_of_sol_obj
    }

    return render(request,
                  'api_frontends/solar_system_objects_overview.html',
                  context)


def sol_obj_detail(request, slug):
    sol_obj = get_object_or_404(SolarSystemObject, slug=slug)

    context = {
        "sol_obj": sol_obj
    }

    return render(request, 'api_frontends/solar_system_object_detail.html', context)

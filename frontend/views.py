from django.shortcuts import render, get_object_or_404

from messier_objects.models import MessierObject
from solar_system_objects.models import SolarSystemObject
from asteroids_comets_meteors.models import AsteroidCometMeteorObject

from utils.frontend_view_utils import overview_post_request


def index(request):
    return render(request, 'index.html')


def mes_obj_overview(request):

    if request.method == 'POST':
        list_of_mes_obj = overview_post_request(request)
        # else if not post request.
    else:
        list_of_mes_obj = MessierObject.objects.all()

    context = {
        "list_of_mes_obj": list_of_mes_obj
    }

    return render(request,
                  'api_frontends/messier_objects_overview.html', context)


def mes_obj_detail(request, mes_num):
    mes_obj = get_object_or_404(MessierObject, messier_number=mes_num)

    context = {
        "mes_obj": mes_obj
    }

    return render(request, 'api_frontends/messier_object_detail.html', context)


def sol_obj_overview(request):

    if request.method == 'POST':
        list_of_sol_obj = overview_post_request(request)
    # else if not post request.
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

    return render(request,
                  'api_frontends/solar_system_object_detail.html', context)


def acm_obj_overview(request):

    if request.method == 'POST':
        list_of_acm_obj = overview_post_request(request)
    # else if not post request.
    else:
        list_of_acm_obj = AsteroidCometMeteorObject.objects.all()

    context = {
        "list_of_acm_obj": list_of_acm_obj
    }

    return render(request,
                  'api_frontends/asteroids_comets_meteors_overview.html',
                  context)


def acm_obj_detail(request, slug):
    acm_obj = get_object_or_404(AsteroidCometMeteorObject, slug=slug)

    context = {
        "acm_obj": acm_obj
    }

    return render(request,
                  'api_frontends/asteroids_comets_meteors_detail.html',
                  context)

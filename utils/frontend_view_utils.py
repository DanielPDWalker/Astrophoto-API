from django.shortcuts import render, get_object_or_404

from messier_objects.models import MessierObject
from solar_system_objects.models import SolarSystemObject
from asteroids_comets_meteors.models import AsteroidCometMeteorObject


def overview_post_request(request):
    # request.path_info returns one of the strings below, based
    # on where the request was sent from. We just use the model_dict
    # to choose the correct model for selected objects.
    model_dict = {
        '/messier_objects': MessierObject,
        '/asteroids_comets_meteors': AsteroidCometMeteorObject,
        '/solar_system_objects': SolarSystemObject
    }

    if 'captured_only_button' in request.POST:
        return model_dict[request.path_info].objects.filter(captured=True)
    if 'not_captured_only_button' in request.POST:
        return model_dict[request.path_info].objects.filter(captured=False)
    if 'reset_filters_button' in request.POST:
        return model_dict[request.path_info].objects.all()

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from frontend import views


urlpatterns = [
    path('', views.index, name='index'),
    path('messier_objects', views.mes_obj_overview, name='mes_obj_overview'),
    path('messier_objects/<int:mes_num>',
         views.mes_obj_detail, name='mes_obj_detail'),
    path('solar_system_objects', views.sol_obj_overview,
         name='sol_obj_overview'),
    path('solar_system_objects/<str:slug>',
         views.sol_obj_detail, name='sol_obj_detail'),
    path('asteroids_comets_meteors',
         views.acm_obj_overview, name='acm_obj_overview'),
    path('asteroids_comets_meteors/<str:slug>',
         views.acm_obj_detail, name='acm_obj_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

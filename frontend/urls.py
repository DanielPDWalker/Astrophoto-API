from django.urls import path, include

from frontend import views


urlpatterns = [
    path('', views.index, name='index'),
    path('messier_objects', views.mes_obj_overview, name='mes_obj_overview'),
    path('messier_object_detail', views.mes_obj_detail, name='mes_obj_detail')
]

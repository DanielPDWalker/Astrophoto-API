from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from frontend import views


urlpatterns = [
    path('', views.index, name='index'),
    path('messier_objects', views.mes_obj_overview, name='mes_obj_overview'),
    path('messier_object_detail', views.mes_obj_detail, name='mes_obj_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

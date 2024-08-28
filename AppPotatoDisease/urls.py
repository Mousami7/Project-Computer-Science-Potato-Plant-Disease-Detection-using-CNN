from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from AppPotatoDisease.fastapi_app.main import ping
urlpatterns = [
    path('', views.home, name='home'),
    path('base/',views.base,name='base'),
    path('upload_image/',views.upload_image,name="upload_image"),
    path('ping', ping,name='ping'),
    path('realtime_detection/', views.realtime_detection, name='realtime_detection'),

    


]

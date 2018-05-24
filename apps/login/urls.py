from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.landing),
    url(r'^login$', views.log_reg),
    url(r'^processRegistration$', views.registration),
    url(r'^processLogin$', views.login),
    url(r'^travels$', views.landing),
   
]

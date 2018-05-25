from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.landing),
    url(r'^enter', views.enter),
    url(r'^login$', views.log_reg),
    url(r'^processRegistration$', views.registration),
    url(r'^processLogin$', views.login),
]

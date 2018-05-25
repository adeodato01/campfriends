from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^info$', views.info, name='info'),
	url(r'^add_info/(?P<location>\S+)', views.add_info, name='add_info'), #the \S allows for any characters to be in the GET
	url(r'^process_info$', views.process_info, name='process_info'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^travels$', views.travels, name='travels'),
]
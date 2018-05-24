from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.info),
	url(r'^campfriends/info$', views.info, name='info'),
	url(r'^campfriends/add_info$', views.add_info, name='add_info'),
	url(r'^campfriends/process_info$', views.process_info, name='process_info'),
]
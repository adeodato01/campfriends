from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.info),
	url(r'^info$', views.info, name='info'),
	url(r'^add_info$', views.add_info, name='add_info'),
	url(r'^process_info$', views.process_info, name='process_info'),
]
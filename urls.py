from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

urlpatterns = [
    url(r'^$', views.index,name = 'index'),
   url(r'^login', views.login),
   url(r'^register',views.register),
   url(r'^nearby',views.nearby),
]

urlpatterns = format_suffix_patterns(urlpatterns)

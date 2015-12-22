from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from swim_api_functions import views

urlpatterns = [
    url(r'^businesstype/$', views.businesstype),
    #url(r'^business/$', views.business),
    url(r'^business/(?P<pk>[0-9]+)/$', views.business),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
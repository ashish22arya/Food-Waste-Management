from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/$',views.StudentList.as_view()),
    url(r'^api/(?P<rollNum>[\w]+)/$', views.StudentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
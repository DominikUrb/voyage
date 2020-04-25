from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^marker/list/$', MarkerList.as_view()),
    url(r'^line/list/$', LineList.as_view()),
]

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^user/list$', UserList.as_view()),
    url(r'^user/create/$', UserCreate.as_view()),
    url(r'user/(?P<pk>\d+)/$', UserRetrieveUpdate.as_view()),
]

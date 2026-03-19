# from django.conf.urls import url
from django.urls import include, re_path

from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

app_name = 'profiles'

urlpatterns = [
    re_path(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    re_path(r'^profiles/(?P<username>\w+)/follow/?$', 
        ProfileFollowAPIView.as_view()),
]

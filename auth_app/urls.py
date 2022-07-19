from urllib.parse import urlparse
from django import views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('signup/',views.SignUp, name='signup'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),

]

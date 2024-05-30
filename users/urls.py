from django.urls import path
from .views import index, home
from .views import MyLoginView

urlpatterns = [
    path("",home , name="home"),
    path("start/", index, name="index"),
    path("login/", MyLoginView.as_view(), name="login"),
]
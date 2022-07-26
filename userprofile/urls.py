from django.urls import path
from .views import Userloginview, user_signup_view, logout_view

app_name = "userprofile"

urlpatterns = [
    path("login/", Userloginview.as_view(),name="login"),
    path("register/", user_signup_view,name="register"),
    path('logout/', logout_view, name="logout"),
]

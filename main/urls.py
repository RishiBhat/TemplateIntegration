from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from .import views



    #First we will include the login and registration credentials


urlpatterns = [

    path('register/', login_view, name="login"),
    path('login/', register_user, name="register"),
    path("dash/", views.dash,  name="dash"),
    path("about/", views.about,  name="about"),

]
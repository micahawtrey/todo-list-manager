from django.urls import path
from accounts.views import signin, signout, signup

urlpatterns = [
    path("login/", signin, name="login"),
    path("logout/", signout, name="logout"),
    path("signup/", signup, name="signup")
]

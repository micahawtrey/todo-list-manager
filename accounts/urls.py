from django.urls import path
from accounts.views import signin, signout

urlpatterns = [
    path("login/", signin, name="login"),
    path("logout/", signout, name="logout"),
]

from django.urls import path
from accounts.views import signin

urlpatterns = [
    path("login/", signin, name="login"),
]

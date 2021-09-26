from django.urls import path
from account.views import *

from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"


urlpatterns = [
    path('signup', signup_view, name="signup"),
    # path('validate', validation_view, name="validate"),
    path('login', obtain_auth_token, name="login")
]
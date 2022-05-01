from django.urls import path
from recaptcha_ak.views import verify

urlpatterns = [
    path('send/', verify)
]
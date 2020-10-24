from django.urls import path, include
# from rest_framework import routers
from mailer.views import send

# router = routers.DefaultRouter()
# router.register(r'mailer', send)

urlpatterns = [
    # path('', include(router.urls)),
    path('send/', send)
]
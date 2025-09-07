from django.urls import path
from app.views import checkout

urlpatterns = [
    path("checkout/<int:order_pk>/", checkout, name="checkout"),
]

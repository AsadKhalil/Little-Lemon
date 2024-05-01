from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuView.as_view()),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("api-token-auth/", obtain_auth_token),
]

from django.urls import path
from .views import RegisterView, LoginView,ResetView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("reset-password/",ResetView.as_view())
]





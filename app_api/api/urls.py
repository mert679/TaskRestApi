from django.urls import path
from .views import registration_view, LoginView, UserCarListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("register/", registration_view, name="register"),
    path("cars/", UserCarListView.as_view(), name="cars"),
 ]
from django.urls import path
from .views import healthtracker
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', healthtracker.index, name="healthtracker"),
    path('register', healthtracker.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='healthtracker/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='healthtracker/logout.html'), name="logout"),
]

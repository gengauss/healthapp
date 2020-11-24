from django.contrib.auth import views as auth_views
from django.urls import path

from .views import healthtracker, goal
from .views.healthtracker import select_food, update_food, delete_food, ProfilePage, add_food

urlpatterns = [
    path('', healthtracker.index, name="healthtracker"),
    path('register', healthtracker.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='healthtracker/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='healthtracker/logout.html'), name="logout"),
    path('forum', healthtracker.forum, name="forum"),
    path('caloriestracker', healthtracker.calories_tracker, name="caloriestracker"),
    path('caloriestracker/select_food/', select_food, name='select_food'),
    path('caloriestracker/add_food/', add_food, name='add_food'),
    path('caloriestracker/update_food/<str:pk>/', update_food, name='update_food'),
    path('caloriestracker/delete_food/<str:pk>/', delete_food, name='delete_food'),
    path('caloriestracker/profile/', ProfilePage, name='profile'),
    path('goalstracker', goal.listGoal, name="goalstracker")
]

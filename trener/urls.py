from django.contrib import admin
from django.urls import path, re_path
from .views import *
from rest_framework.authtoken import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth', views.obtain_auth_token, name='api-token-auth'),
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('auth', Auth.as_view()),
    path('logout', LogoutView.as_view()),
    path('users', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('weight', WeightView.as_view()),
    path('chest', ChestView.as_view()),
    path('biceps', BicepsView.as_view()),
    path('benchpress', BenchPressView.as_view()),
    path('squat', SquatView.as_view()),
    path('deadlift', DeadliftView.as_view()),
]

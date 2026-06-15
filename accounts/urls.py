from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('logout/', views.logout_view, name='logout'),
]

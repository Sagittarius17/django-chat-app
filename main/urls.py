from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_layout, name='main'),
    path('signin/', views.user_login, name='signin'),
    path('signup/', views.signup, name='signup'),
]

from . import views
from django.urls import path

urlpatterns = [
path('register/',views.UserRegisterView.as_view(),name='register'),
path('update/',views.UserChangeView.as_view(),name='update'),
path('password/',views.PasswordsChangeView.as_view(),name='password'),
    #path('login',),

    ]
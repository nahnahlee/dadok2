from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('me/', views.me, name='me'),
    path('delete/', views.delete_user, name='delete_user'),
]

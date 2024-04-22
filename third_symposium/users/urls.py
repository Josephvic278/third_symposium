from django.urls import path
from .views import *

<<<<<<< HEAD
app_name = 'user'

urlpatterns = [
    path('register/', register, name='registerPage'),

=======
app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', signIn, name='login'),
    path('logout/', logout, name='logout')
>>>>>>> 57e91d4c8e93447a6f16f6dc9e85f630f45fcf04
]
from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('register/', register, name='registerPage'),

]
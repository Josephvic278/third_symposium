from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('dashboard/', dashboard, name='dashboard')
]
from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', landing_page, name='indexPage'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactList.as_view(), name='ContactList'),
    path('<int:id>/', ContactDetail.as_view(), name='ContactDetail'),
]
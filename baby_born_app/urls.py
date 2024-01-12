from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('doctors/<str:group>', doctors, name="doctors"),
    path('babies/<str:type>', babies, name="babies"),
    path('hospital', hospital, name="hospital"),
]
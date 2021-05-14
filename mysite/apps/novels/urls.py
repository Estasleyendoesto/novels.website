from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', NovelView.as_view(), name='novel'),
    path('<slug:slug>/<int:choice>/', NovelView.as_view(), name='novel')
]
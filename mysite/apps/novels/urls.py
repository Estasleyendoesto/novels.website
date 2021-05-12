from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', NovelView.as_view(), name='novel'),
    path('<int:pk>/<int:choice>/', NovelView.as_view(), name='novel')
]
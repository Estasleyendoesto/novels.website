from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ContribEditorView.as_view(), name='contrib_editor'),
]
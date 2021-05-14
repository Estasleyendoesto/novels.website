from django.urls import path
from .views import *

urlpatterns = [
    path('', ContribEditorView.as_view(), name='contrib_editor'),
]
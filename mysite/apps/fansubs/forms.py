from django import forms
from .models import Contrib


class ContribForm(forms.ModelForm):

    class Meta:
        model = Contrib
        fields = ['content',]

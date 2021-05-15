from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy

from .models import Contrib
from .forms import ContribForm

class ContribEditorView(UpdateView):
    template_name = 'fansubs/contrib_editor.html'
    form_class = ContribForm
    model = Contrib

    def get_success_url(self):
        return reverse_lazy('contrib_editor', args=[self.get_object().pk])
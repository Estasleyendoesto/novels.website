from django.urls.base import reverse
from django.views.generic.edit import FormView

from django.urls import reverse_lazy

from .forms import QuillFieldForm
from .models import Contrib


class ContribEditorView(FormView):
    template_name = 'fansubs/contrib_editor.html'
    form_class = QuillFieldForm
    success_url = reverse_lazy('contrib_editor')

    def post(self, *args, **kwargs):
        print('------------------------>', 'ahoyy!') 
        return super().post(*args, **kwargs)

    def form_valid(self, form):
        print('----------------->', 'eeeeeeeeeeeeeeeeeeeee')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
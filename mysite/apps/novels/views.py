from django.views.generic.detail import DetailView

from .models import Novel
from ..likes.views import LikesMixin

class NovelView(LikesMixin, DetailView):
    template_name = 'novels/novel.html'
    context_object_name = 'novel'
    model = Novel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Temporal
        context['likeslist'] = self.get_object().likes.all()

        return context
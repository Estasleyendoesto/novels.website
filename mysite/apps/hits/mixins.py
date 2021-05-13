from .managers import HitsLogManager
from .models import HitsLog
from .utils import get_ip 


class HitsMixin:
    """
    Solo puede usarse con DetailView o UpdateView
    """

    keep_hit_active = {'days': 7}
    max_hits_per_ip = 0

    def hit_eval(self, request):
        # A partir de la 1.8.4 las sesiones vacías no se guardan
        if request.session.session_key is None:
            request.session.save()

        ip          = get_ip(request)
        user        = request.user
        user_agent  = request.META.get('HTTP_USER_AGENT', '')[:255]
        session_key = request.session.session_key
        active_hits = HitsLog.objects.filter_active(self.keep_hit_active)
        


        print('OKKKK')
    
    def dispatch(self, request, *args, **kwargs):
        if request.method in ('GET', 'POST'):
            self.hit_eval(request)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
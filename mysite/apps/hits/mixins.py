from .managers import HitsLogManager
from .models import Hit, HitsLog, BlacklistIP, BlacklistUA
from .utils import get_ip 


class HitsMixin:
    """
    Solo puede usarse con DetailView, UpdateView, TemplateView... 
    (Porque básicamente requiere un objeto, o usar el atributo custom_object)
    """
    keep_hit_active = {'days': 7}
    max_hits_per_ip = 0
    object_to_hit = None    # Mymodel.objects.get(...)
    hit = None

    def hit_eval(self, request):
        # A partir de la 1.8.4 las sesiones vacías no se guardan
        if request.session.session_key is None:
            request.session.save()

        ip          = get_ip(request)
        user        = request.user
        user_agent  = request.META.get('HTTP_USER_AGENT', '')[:255]
        session_key = request.session.session_key
        object      = self.object_to_hit
    
        if not object:
            object  = self.object_to_hit()

        try:
            hit = object.hits.get()
        except Hit.DoesNotExist:
            hit = object.hits.create()

        self.hit = hit

        # Si está baneado return None
        if BlacklistIP.objects.filter(ip__exact=ip):
            return None
        if BlacklistUA.objects.filter(user_agent__exact=user_agent):
            return None

        # Obtenemos todos los HitLogs según hora y fecha deseada
        active_hits = HitsLog.objects.filter_active(self.keep_hit_active)

        # Si un IP supera el máximo de visitas return None
        if self.max_hits_per_ip:
            if active_hits.filter(ip__exact=ip).count() >= self.max_hits_per_ip:
                return None
        
        # Creamos el objeto HitLog
        hit_log = HitsLog(ip=ip, session=session_key, user_agent=user_agent, hit=hit)

        # Guardamos el objeto HitsLog en la BD
        if user.is_authenticated:
            if not active_hits.filter(user=user, hit=hit):
                hit_log.user = user
                hit_log.save()
                return True
        else:
            if not active_hits.filter(session=session_key, hit=hit):
                hit_log.save()
                return True
    
    def dispatch(self, request, *args, **kwargs):
        if request.method in ('GET', 'POST'):
            if self.hit_eval(request):
                self.hit.hits += 1
                self.hit.save()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hits'] = self.hit.hits
        return context

    def get_custom_object(self, )0
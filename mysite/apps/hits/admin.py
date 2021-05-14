from django.contrib import messages
from django.utils.translation import ngettext

from django.contrib import admin

from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from .models import Hit, HitsLog

@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ['source', 'object', 'hits', 'last_hit']
    list_filter  = ('hits', 'last_hit')
    search_fields = ['hits', 'last_hit']
    show_full_result_count = True

    def source(self, obj):
        return obj.object.__class__.__name__


@admin.register(HitsLog)
class HitsLogAdmin(admin.ModelAdmin):
    list_display  = ['creation_date', 'user', 'ip', 'user_agent', 'object']
    list_filter   = ('creation_date',)
    search_fields = ['ip', 'user__username', 'user_agent']
    list_display_links = None
    show_full_result_count = True
    actions = ['clean_logs']

    def object(self, obj):
        return obj.hit.object

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_action_choices(self, request):
        choices = super().get_action_choices(request)
        choices.pop(0)
        choices.reverse()
        return choices

    @admin.action(description='Elimina todos los registros antiguos')
    def clean_logs(self, request, queryset):
        limit = getattr(settings, 'KEEP_HITSLOGS_IN_DB', {'days': 30})
        period = timezone.now() - timedelta(**limit)
        hits_logs = queryset.filter(creation_date__lt=period)
        deletions = hits_logs.count()
        hits_logs.delete()

        self.message_user(request, ngettext(
            '%d registro eliminado con éxito',
            '%d registros eliminados con éxito',
            deletions,
        ) % deletions, messages.SUCCESS)

    
from django.contrib import admin
from .models import Hit, HitsLog

@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ['source', 'object', 'hits', 'last_hit']
    list_filter  = ('hits', 'last_hit')
    search_fields = ['object', 'hits', 'last_hit']
    show_full_result_count = True

    def source(self, obj):
        return obj.object.__class__.__name__


@admin.register(HitsLog)
class HitsLogAdmin(admin.ModelAdmin):
    list_display  = ['creation_date', 'user', 'ip', 'user_agent', 'object']
    list_filter   = ('creation_date',)
    search_fields = ['ip', 'user', 'hit', 'user_agent']
    list_display_links = None
    show_full_result_count = True

    def object(self, obj):
        return obj.hit.object

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
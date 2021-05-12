from django.contrib import admin
from .models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display  = ['source', 'object', 'user', 'like', 'creation_date']
    list_filter   = ('like', 'creation_date')
    search_fields = ['object', 'user', 'like']
    ordering      = ['creation_date']
    list_display_links = None
    show_full_result_count = True

    def source(self, obj):
        return obj.object.__class__.__name__

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
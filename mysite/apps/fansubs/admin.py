from django.contrib import admin
from .models import Contrib

@admin.register(Contrib)
class ContribAdmin(admin.ModelAdmin):
    pass
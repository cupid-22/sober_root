from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User

admin.site.unregister(Group)


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('id', 'social_id', 'social_type')
    search_fields = ('id', 'social_id', 'social_type')
    fields = (('social_id', 'social_type'), ('date_joined', 'last_login'))
    readonly_fields = ('last_login', 'date_joined')
    ordering = ['-id']
    list_filter = ['social_type']
    view_on_site = False

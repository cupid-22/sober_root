from django.contrib import admin
from .models import Literature, LiteratureSubSection


class LiteratureSubSectionAdmin(admin.StackedInline):
    model = LiteratureSubSection
    fields = ('title', ('is_sub_title_active', 'sub_title'), 'main_content')
    extra = 6


@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title')
    search_fields = ('id', 'title', 'sub_title')
    fields = ('title', 'sub_title')
    ordering = ['-id']
    list_filter = ['title']
    view_on_site = False

    inlines = [
        LiteratureSubSectionAdmin
    ]


@admin.register(LiteratureSubSection)
class LiteratureSubSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'literature_id', 'title', 'sub_title', 'main_content')
    search_fields = ('id', 'title', 'sub_title', 'main_content')
    fields = ('title', ('is_sub_title_active', 'sub_title'), 'main_content', 'literature_id',)
    ordering = ['-id']
    view_on_site = False

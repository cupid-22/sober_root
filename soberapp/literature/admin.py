from django.contrib import admin
from .models import Literature, LiteratureSubSection


class LiteratureSubSectionAdmin(admin.StackedInline):
    model = LiteratureSubSection
    fields = ('title', ('start_page', 'end_page'), 'subtitle', 'main_content')
    extra = 3


@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'is_subtitle_active', 'is_sequence_active')
    fields = ('title', 'subtitle', 'is_subtitle_active', 'is_sequence_active')
    search_fields = ('id', 'title', 'subtitle')
    ordering = ['-id']
    list_filter = ['is_subtitle_active', 'is_sequence_active']
    view_on_site = False

    inlines = [
        LiteratureSubSectionAdmin
    ]


@admin.register(LiteratureSubSection)
class LiteratureSubSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'literature', 'title', 'subtitle', 'main_content')
    search_fields = ('id', 'title', 'subtitle', 'main_content')
    fields = ('title', 'subtitle', 'main_content', 'literature',)
    list_filter = ['literature']
    ordering = ['-id']
    view_on_site = False

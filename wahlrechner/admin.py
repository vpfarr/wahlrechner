from django.contrib import admin
from .models import These, Antwort, Partei
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class TheseResource(resources.ModelResource):
    class Meta:
        model = These


class TheseAdmin(ImportExportModelAdmin):
    list_display = ['these_nr', 'these_keyword', 'these_text']
    list_display_links = ['these_keyword']
    ordering = ['these_nr']
    search_fields = ['these_keyword', 'these_text']
    resource_class = TheseResource


class AntwortResource(resources.ModelResource):
    class Meta:
        model = Antwort


class AntwortAdmin(ImportExportModelAdmin):
    list_display = ['antwort_partei',
                    'antwort_these', 'antwort_position']
    list_display_links = ['antwort_partei', 'antwort_these']
    search_fields = ['antwort_these', 'antwort_partei']
    list_filter = ['antwort_partei']
    autocomplete_fields = ['antwort_these', 'antwort_partei']
    resource_class = AntwortResource


class ParteiResource(resources.ModelResource):
    class Meta:
        model = Partei


class ParteiAdmin(ImportExportModelAdmin):
    search_fields = ['partei_name']
    resource_class = ParteiResource


admin.site.register(These, TheseAdmin)
admin.site.register(Antwort, AntwortAdmin)
admin.site.register(Partei, ParteiAdmin)

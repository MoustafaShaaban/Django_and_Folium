from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Feature
from .resources import FeatureResource


class FeatureAdmin(ImportExportModelAdmin):
    resource_class = FeatureResource


admin.site.register(Feature, FeatureAdmin)

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Hospital, School, Library
from .resources import HospitalResource, SchoolResource, LibraryResource


class HospitalAdmin(ImportExportModelAdmin):
    resource_class = HospitalResource


class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource


class LibraryAdmin(ImportExportModelAdmin):
    resource_class = LibraryResource


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Library, LibraryAdmin)

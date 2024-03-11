from import_export import resources
from .models import Hospital, School, Library


class HospitalResource(resources.ModelResource):
    class Meta:
        model = Hospital


class SchoolResource(resources.ModelResource):
    class Meta:
        model = School


class LibraryResource(resources.ModelResource):
    class Meta:
        model = Library
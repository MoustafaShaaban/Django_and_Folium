from import_export import resources

from .models import Feature


class FeatureResource(resources.ModelResource):

    class Meta:
        model = Feature
        exclude = ('pk',)
        skip_unchanged = True
        report_skipped = False
        
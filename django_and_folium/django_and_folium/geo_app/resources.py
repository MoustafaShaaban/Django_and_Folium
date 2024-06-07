from import_export import resources

from .models import Feature


class FeatureResource(resources.ModelResource):

    class Meta:
        model = Feature
        exclude = ('pk', 'owner')
        skip_unchanged = True
        report_skipped = False

    def after_import_instance(self, instance, new, **kwargs):
        instance.owner = kwargs['user']

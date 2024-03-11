from rest_framework import serializers

from geoapp.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ["name", "type", "description", "latitude", "longitude", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:feature-detail", "lookup_field": "id"}
        }
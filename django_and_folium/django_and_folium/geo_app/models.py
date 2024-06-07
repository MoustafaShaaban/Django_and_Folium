from django.conf import settings
from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=250, help_text='Feature Name')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='features',
        help_text='Feature Owner',
        null=True,
    )
    description = models.TextField(help_text='Feature Description')
    type = models.CharField(max_length=100, help_text='Feature Type (Hotel, Hospital, School, Park, ...)')
    latitude = models.FloatField(help_text='Latitude')
    longitude = models.FloatField(help_text='Longitude')


    class Meta:
        verbose_name = ("feature")
        verbose_name_plural = ("features")

    def __str__(self):
        return f'{self.name}, {self.type}'

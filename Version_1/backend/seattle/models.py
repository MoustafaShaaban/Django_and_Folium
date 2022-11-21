from django.db import models


class Hospital(models.Model):
    """ Model Class represents each Hospital in Seattle """
    facility = models.CharField(max_length=250, null=True, default='test')
    address = models.CharField(max_length=250, null=True, default='test')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitals"

    def __str__(self):
        """Return string representation of the model"""
        return self.facility


class School(models.Model):
    """ Model class represents Public School in Seattle """
    name = models.CharField(max_length=250, null=True, default='test')
    address = models.CharField(max_length=250, null=True, default='test')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        """Return string representation of the model"""
        return self.name


class Library(models.Model):
    """Model class represents a Library in Seattle"""
    name = models.CharField(max_length=250, null=True, default='test')
    address = models.CharField(max_length=250, null=True, default='test')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

    def __str__(self):
        """Return string representation of the model"""
        return  self.name

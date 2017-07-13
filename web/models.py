# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class TimeStamped(models.Model):
    creation_date = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Site(TimeStamped):

    name = models.CharField(max_length=30, unique=True, blank=False)


class SiteDetail(TimeStamped):

    site = models.ForeignKey(Site, default=None, on_delete=models.CASCADE)
    detail_date = models.DateField(null=False)
    a_value = models.FloatField(null=False)
    b_value = models.FloatField(null=False)

    class Meta:
        ordering = ('detail_date', )

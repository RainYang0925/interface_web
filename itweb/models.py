# -*- coding: utf-8 -*-
from django.db import models


class IT(models.Model):
    it_name = models.CharField(max_length=30, primary_key=True)
    host = models.CharField(max_length=30)
    request_type = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    args = models.CharField(max_length=300)

    # author = models.CharField(max_length=30)

    def __unicode__(self):
        return self.it_name


class NewIT(models.Model):
    it_name = models.CharField(max_length=30, primary_key=True)
    protocol_type = models.CharField(max_length=10)
    request_type = models.CharField(max_length=10)
    url = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    team = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    def __unicode__(self):
        return self.it_name

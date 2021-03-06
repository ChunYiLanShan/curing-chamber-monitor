# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from pocket_monitor.db import models


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = '__all__'
        depth = 1

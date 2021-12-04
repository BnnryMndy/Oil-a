from django.db import models


class Entity(models.Model):
    Entity_id = models.IntegerField('Entity_id')
    Position = models.TextField('position')
    create_time = models.TimeField('create_time')
    danger_id = models.IntegerField('danger_id')
    area = models.FloatField('area')
    status_id = models.IntegerField('status_id')
    pipeline_id = models.IntegerField('pipeline_id')


class danger_levels(models.Model):
    danger_id = models.IntegerField('danger_id')
    name = models.TextField('name')
    description = models.TextField('description')
    rules = models.TextField('rules')
    color = models.TextField('color')


class Entity_source(models.Model):
    Entity_id = models.IntegerField('Entity_id')
    source_id = models.IntegerField('source_id')


class source(models.Model):
    source_id = models.IntegerField('source_id')
    name = models.TextField('name')
    description = models.TextField('description')


class oil_company(models.Model):
    oil_company_id = models.IntegerField('oil_company_id')
    name = models.TextField('name')
    description = models.TextField('description')


class contragents(models.Model):
    contragent_id = models.IntegerField('contragent_id')
    name = models.TextField('name')
    description = models.TextField('description')


class oil_pipeline(models.Model):
    oil_pipeline_id = models.IntegerField('oil_pipeline_id')
    name = models.TextField('name')
    description = models.TextField('description')


class comments(models.Model):
    comment_id = models.IntegerField('comment_id')
    name = models.TextField('name')
    comment = models.TextField('comment')


class status(models.Model):
    status_id = models.IntegerField('status_id')
    name = models.TextField('name')
    description = models.TextField('description')


class media(models.Model):
    media_id = models.IntegerField('media_id')
    name = models.TextField('name')
    description = models.TextField('description')



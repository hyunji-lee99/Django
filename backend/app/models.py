from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField as JSONBField


# Create your models here.
class Post(models.Model):
    data = JSONBField(default=list)

class Sep(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

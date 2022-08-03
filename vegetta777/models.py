from django.db import models

# Create your models here.
class djmariio(models.Model):
    nombre = models.CharField(max_length=20)
    canalYOUTUBE = models.CharField(max_length=20)

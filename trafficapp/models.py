from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TrafficGenerateRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    minimum = models.IntegerField()
    maximum = models.IntegerField()
    requests = models.IntegerField()
    stay = models.IntegerField()

    def __str__(self):
        return self.user.username
from django.db import models

class Establishment(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

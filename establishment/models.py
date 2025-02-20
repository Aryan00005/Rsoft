from django.db import models

class EstablishmentBasic(models.Model):
    name = models.CharField(max_length=200,verbose_name="Establishment Name")
    state = models.CharField(max_length=100,verbose_name="State")
    type = models.CharField(max_length=100,verbose_name="Establishment Type")

    def __str__(self):
        return self.name
    


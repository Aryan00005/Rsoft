from django.db import models

class Act(models.Model):
    name = models.CharField(max_length=255,blank=True,verbose_name="Act Name") 
    form_name = models.CharField(max_length=255, blank=True,verbose_name="Form / Register Name")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

  
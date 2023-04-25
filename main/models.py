from django.db import models

# Create your models here.
class Language(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    piston_language = models.CharField(max_length=100, null=False, blank=False)
    piston_version = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.title

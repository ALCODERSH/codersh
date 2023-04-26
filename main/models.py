from django.db import models
from uuid import uuid4

# Create your models here.


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    ace_mode = models.CharField(max_length=60, null=False, blank=False)
    piston_language = models.CharField(max_length=100, null=False, blank=False)
    piston_version = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class AceTheme(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    ace_theme = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class AceFont(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    prompt = models.TextField(null=False, blank=False)
    input = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return str(self.id)
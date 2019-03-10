from django.db import models

class Job(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

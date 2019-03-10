from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField(blank=True)
    finish_date = models.DateField(blank=True)
    description = models.TextField()
    additional_link = models.URLField(max_length=256, blank=True)
    image = models.ImageField(upload_to='images/')

from django.db import models

class Blog(models.Model):
        title = models.CharField(max_length=256)
        publication_date = models.DateField(blank=True)
        post_content = models.TextField()
        image = models.ImageField(upload_to='images/')

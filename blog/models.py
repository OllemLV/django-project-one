from django.db import models

class Blog(models.Model):
        title = models.CharField(max_length=256)
        publication_date = models.DateField(blank=True)
        post_content = models.TextField()
        image = models.ImageField(upload_to='images/')

        def summary(self):
            if len(self.post_content)>=64:
                return self.post_content[:64]+'...'
            else:
                return self.post_content[:64]

        def publication_date_better(self):
            return self.publication_date.strftime('%b %e %Y')

        def __str__(self):
            return self.title

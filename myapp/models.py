from django.db import models

# Create your models here.

class Blog (models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    upload = models.FileField(upload_to='uploads/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

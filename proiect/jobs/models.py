from django.db import models


class Job(models.Model):

    job_type = models.IntegerField()
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.job_type} - {self.title} - {self.url} - {self.description}"

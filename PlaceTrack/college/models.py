from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    locations = models.TextField()
    job_description = models.TextField()
    no_of_opportunities = models.IntegerField()

    def __str__(self):
        return self.company_name
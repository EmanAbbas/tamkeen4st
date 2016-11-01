"""
Definition of models.
"""
import django.core.management

from django.db import models

# Create your models here.
class Sponsor(models.Model):
        name=models.CharField( max_length=250)
        notes=models.TextField(blank=True, null=True)
        photo=models.ImageField(upload_to='uploads')
        link=models.CharField(max_length=250)


        def __str__(self):
            return self.name

class Subscriber(models.Model):
        name=models.CharField(max_length=200)
        email=models.EmailField()
        def __str__(self):
            return self.name
        #publishesAt=models.DateField()
        #author=models.ForeignKey(Author)
         #if here foreign key field

class Project(models.Model):
    project_name=models.CharField(max_length=200)
    description=models.TextField()
    video=models.FileField(blank=True, null=True)
    topics_covered=models.TextField()
    notes=models.CharField(max_length=500)

    def __str__(self):
        return self.project_name
    def short_description(self):
        return self.description[0:130]+"..."





class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    enquiry=models.TextField()
    def __str__(self):
        return self.name
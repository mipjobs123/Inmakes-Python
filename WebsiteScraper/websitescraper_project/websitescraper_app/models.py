from django.db import models

# Create your models here.
class Links(models.Model):

    def __str__(self):
        return self.stringname1
    address = models.CharField(max_length=500,null=True,blank=True)      #www.google.com
    stringname1= models.CharField(max_length=500,null=True,blank=True)    #google




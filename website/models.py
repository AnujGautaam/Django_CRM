from django.db import models
import datetime

# Create your models here.
# this is where all the models for the database go and this is where all the magic for the schemas or what not takes place 
# the first and foremost thing to understand here is that we are creating a class for this as well and this is not that even hard 
class Record(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True,default='000000000')
    # born_at = models.DateTimeField()
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
   


    def __str__(self):
        return (f"{self.city} {self.last_name}")
    
# this is the page where the model is used and selected 
# this is schema and the schema is used for recording the different aspects 
# there is so much of similarities with schema that i will be calling it a schema as well
# one of the issues that i ran into was with the records model which didnt allow me to edit the required fields to make it easier for me to do this editing  


class Record1(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True,default='000000000')
    # born_at = models.DateTimeField()
    initial_name =models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.initial_name} {self.family_name}")
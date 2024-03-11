from django.db import models
from django.core.exceptions import ValidationError

def characters_only(value):
    if any(char.isdigit() for char in value):
        raise ValidationError("Only characters are allowed in Name")

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200, validators=[characters_only])  
   last_name = models.CharField(max_length=200, validators=[characters_only])
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   description = models.CharField(max_length=1000,default='')
   def __str__(self):
      return self.name

class Feedback(models.Model):
   Give_a_Valueable_feedback = models.CharField(max_length=1000, default='')

   def __str__(self) -> str:
      return self.Give_a_Valueable_feedback

  
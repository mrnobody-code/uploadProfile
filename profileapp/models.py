from django.db import models

# Create your models here.
class Profile(models.Model):
    # TODO: Define fields here
    Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to= 'images/')


    class Meta:
    	verbose_name = "Profile"
    	verbose_name_plural = "Profiles"

    	def __str__(self):
    		pass
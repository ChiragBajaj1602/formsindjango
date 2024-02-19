from django.db import models

# Create your models here.
class userprofile(models.Model):
    image=models.ImageField(upload_to="images")

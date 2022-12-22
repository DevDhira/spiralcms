from django.db import models
from blog.models import Author,BlogPost
from django.db.models import Sum

# Create your models here.

country_choices = (("United States","United States"),("India","India"),("Africa","Africa"),("Russia","Russia"))

class AuthorProfile(models.Model):
    username = models.OneToOneField(Author,on_delete=models.CASCADE,primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200) 
    location = models.CharField(max_length=400,choices=country_choices)
    current_role = models.CharField(max_length=400)
    about = models.TextField()
    total_views  = models.IntegerField(default=0 ,null=True,blank=True)

    def __str__(self):
        return str(self.username)

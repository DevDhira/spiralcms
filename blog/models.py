
from datetime import datetime, timezone

from django.db import models
from django.contrib.auth import get_user_model



Author = get_user_model()

cat_choices = (("Digital Marketing","Digital Marketing"),("Technology","Technology"))


class BlogPost(models.Model):
    title = models.CharField(max_length=500,unique=True)
    content = models.TextField()
    excerpt=models.TextField()
    image=models.CharField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.today)
    category = models.CharField(choices=cat_choices , max_length=100)
    urlslug = models.SlugField(max_length=500,primary_key=True)
    post_views = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"


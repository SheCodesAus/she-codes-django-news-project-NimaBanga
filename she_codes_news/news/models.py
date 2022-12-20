from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):     
    class Meta:
        ordering = ["-pub_date"]
        verbose_name_plural = "News Stories"
        
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="stories")
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(max_length=200, blank=True) 
    favourited_by = models.ManyToManyField(
        get_user_model(), related_name= "favourites", blank=True
        )
    

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name
#from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model 
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField() 
    date = models.DateTimeField(auto_now_add=True)
    author  = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    
    def __str__(self):
        return "{}. {}".format(self.id,self.title)
    
    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.comment)
    
    def get_absolute_url(self):
        return reverse('list')
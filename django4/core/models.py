from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_about = models.TextField()
    post_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.post_title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})
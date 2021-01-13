from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

class Comments(models.Model):
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
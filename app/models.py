from django.db import models

# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='person/',null=True,blank=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=200, null=True)


    def __str__(self):
        return f"{self.full_name}"
    
# class StudentPoint(models.Model):
    # student = models.ForeignKey(Person, on_delete=models.PROTECT)
    # point = models.CharField(max_length=300)

class Movie(models.Model):
    release_data =models.DateField(auto_now_add=True)
    Description =models.TextField()
    quality=models.CharField(max_length=10,null=True)
    duration=models.CharField(max_length=10,null=True)

class Genre():
    Genre_name=models.CharField(max_length=10,null=True)






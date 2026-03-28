from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=100)
    Brand = models.CharField(max_length=50)

    description = models.TextField()

    On_Road_Price = models.CharField(max_length=50)
    Fixed_Price = models.CharField(max_length=50, blank=True)

    Engine = models.CharField(max_length=50, blank=True)
    Power = models.CharField(max_length=50, blank=True)
    No_of_cylinder = models.CharField(max_length=10, blank=True)
    Gear_box = models.CharField(max_length=50, blank=True)

    phone = models.CharField(max_length=15)
    location = models.URLField(max_length=500, blank=True)

    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)

    Image = models.ImageField(upload_to='items/')
    Image2 = models.ImageField(upload_to='items/', blank=True, null=True)
    Image3 = models.ImageField(upload_to='items/', blank=True, null=True)
    Image4 = models.ImageField(upload_to='items/', blank=True, null=True)
    Image5 = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='feedback/', blank=True)

    def __str__(self):
        return self.User_name

class Offer(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    discount = models.IntegerField(help_text="Discount percentage")
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title    
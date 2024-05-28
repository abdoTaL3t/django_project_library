from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    status_books = [
        ('avaible','avaible'),
        ('rentel','rentel'),
        ('solid','soild')
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length= 250)
    photo_book = models.ImageField(upload_to='photos', null= True, blank= True)
    photo_author = models.ImageField(upload_to='photos', null= True, blank= True)
    pages = models.IntegerField(null= True , blank= True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank= True, null= True)
    relat_price_day = models.DecimalField(max_digits= 5 , decimal_places= 2 , blank= True , null= True)
    relat_period = models.IntegerField( null= True , blank= True)
    active = models.BooleanField(default= True)
    status = models.CharField(max_length= 100 , choices = status_books ,null= True , blank= True ) 
    category = models.ForeignKey(Category, on_delete=models.PROTECT , null= True , blank= True)
    
    def __str__(self):
        return self.title
    
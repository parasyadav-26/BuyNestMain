from django.db import models

class UserData(models.Model):
    
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField()
    password= models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')  # Ensure you have media settings
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
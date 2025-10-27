from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    published_date = models.DateField()
    genre = models.CharField(max_length=50, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
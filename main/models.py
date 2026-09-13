from django.db import models

class Author(models.Model):
    f_name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    b_day = models.CharField(max_length=50)
    
    def __str__(self):
        return super().__str__()
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return super().__str__()    
    
    
from django.db import models

class Author(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    b_date = models.CharField(max_length=50)

    def __str__(self):
        return self.f_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
    
    

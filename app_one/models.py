from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    paint = models.TextField(max_length=250, null=True)

    def __str__(self):
        return f"{self.brand} - {self.year} - {self.paint}"
    
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField(max_length=200)
    release = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return self.title

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField(max_length=250)
    biography = models.TextField(max_length=4000)

    def __str__(self):
        return self.author
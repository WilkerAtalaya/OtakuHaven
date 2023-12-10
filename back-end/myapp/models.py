from django.db import models

# Create your models here.

class User(models.Model):
    user = models.TextField(primary_key=True)
    name = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    password = models.TextField()
    state = models.BooleanField() # 0:False | 1:True
    typeuser = models.TextField() # client or admin

    def __str__ (self):
        return self.user

class Country(models.Model):
    name = models.TextField()

    def __str__ (self):
        return self.name

class Editorial(models.Model):
    name = models.TextField()
    
    def __str__ (self):
        return self.name

class Manga(models.Model):
    name = models.TextField()
    author = models.TextField()
    sinopsis = models.TextField()
    
    def __str__ (self):
        return self.name

class Genre(models.Model):
    name = models.TextField()
    
    def __str__ (self):
        return self.name

class MangaGenre(models.Model):
    idManga = models.ForeignKey(Manga, on_delete = models.CASCADE)
    idGenre = models.ForeignKey(Genre, on_delete = models.CASCADE)

class Volume(models.Model):
    isbn = models.TextField(primary_key=True)
    number = models.IntegerField()
    summary = models.TextField()
    frontpage = models.ImageField()
    manga = models.ForeignKey(Manga, on_delete = models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete = models.CASCADE)
    
    def __str__ (self):
        return self.manga + ' ' + self.number

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    volume = models.ForeignKey(Volume, on_delete = models.CASCADE)
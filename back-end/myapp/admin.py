from django.contrib import admin
from .models import Country, Editorial, Favorite, Genre, Manga, MangaGenre, User, Volume
# Register your models here.

admin.site.register(Country)
admin.site.register(Editorial)
admin.site.register(Favorite)
admin.site.register(Genre)
admin.site.register(Manga)
admin.site.register(MangaGenre)
admin.site.register(User)
admin.site.register(Volume)
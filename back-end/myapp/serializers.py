from rest_framework import serializers
from .models import Country, Editorial, Favorite, Genre, Manga, MangaGenre, User, Volume

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # read_only_fields = ('attribute')
        # Está linea de código límita los campos que no se modificarán
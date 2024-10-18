from rest_framework import serializers
from .models import FavoriteBook


class FavoriteBookSerializer(serializers.ModelSerializer):
   class Meta:
       model = FavoriteBook
       fields = ['user_id', 'title', 'author', 'publication_date', 'rating']

from django.db import models

# Create your models here.
class FavoriteBook(models.Model):
  user_id = models.CharField(max_length = 24)
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  publication_date = models.DateField()
  rating = models.IntegerField()

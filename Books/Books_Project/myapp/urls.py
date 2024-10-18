from django.urls import path
from sqlalchemy.dialects.mssql.information_schema import views


from myapp.views import (
   add_favorite_book,
   read_favorite_book,
   update_favorite_book,
   delete_favorite_book,
)


urlpatterns = [
   path('favorite-books/add/', add_favorite_book, name='add_favorite_book'),  # URL for adding a favorite book
   path('favorite-books/<int:book_id>/', read_favorite_book, name='read_favorite_book'),  # URL for reading a favorite book
   path('favorite-books/update/<int:book_id>/', update_favorite_book, name='update_favorite_book'),  # URL for updating a favorite book
   path('favorite-books/delete/<int:book_id>/', delete_favorite_book, name='delete_favorite_book'),  # URL for deleting a favorite book
]

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import FavoriteBook
import json




# Ajouter un livre favori
@csrf_exempt
def add_favorite_book(request):
  if request.method == 'POST':
      try:
          data = json.loads(request.body)
          book = FavoriteBook(
              user_id=data.get("user_id"),
              title=data.get("title"),
              author=data.get("author"),
              publication_date=data.get("publication_date"),
              rating=data.get("rating")
          )
          book.save()
          return JsonResponse({"message": "Book added successfully", "book_id": book.id}, status=201)
      except Exception as e:
          return JsonResponse({"error": str(e)}, status=400)
  return JsonResponse({"error": "Invalid request method"}, status=405)




# Lire les détails d'un livre favori
def read_favorite_book(request, book_id):
  if request.method == 'GET':
      try:
          book = get_object_or_404(FavoriteBook, id=book_id)
          return JsonResponse({
              "user_id": book.user_id,
              "title": book.title,
              "author": book.author,
              "publication_date": book.publication_date,
              "rating": book.rating
          })
      except FavoriteBook.DoesNotExist:
          return JsonResponse({"error": "Book not found"}, status=404)
      except Exception as e:
          return JsonResponse({"error": str(e)}, status=400)
  return JsonResponse({"error": "Invalid request method"}, status=405)




# Mettre à jour les informations d'un livre favori
@csrf_exempt
def update_favorite_book(request, book_id):
  if request.method == 'PUT':
      try:
          data = json.loads(request.body)
          book = get_object_or_404(FavoriteBook, id=book_id)
          book.title = data.get("title", book.title)
          book.author = data.get("author", book.author)
          book.publication_date = data.get("publication_date", book.publication_date)
          book.rating = data.get("rating", book.rating)
          book.save()
          return JsonResponse({"message": "Book updated successfully"})
      except FavoriteBook.DoesNotExist:
          return JsonResponse({"error": "Book not found"}, status=404)
      except Exception as e:
          return JsonResponse({"error": str(e)}, status=400)
  return JsonResponse({"error": "Invalid request method"}, status=405)




# Supprimer un livre favori
@csrf_exempt
def delete_favorite_book(request, book_id):
  if request.method == 'DELETE':
      try:
          book = get_object_or_404(FavoriteBook, id=book_id)
          book.delete()
          return JsonResponse({"message": "Book deleted successfully"})
      except FavoriteBook.DoesNotExist:
          return JsonResponse({"error": "Book not found"}, status=404)
      except Exception as e:
          return JsonResponse({"error": str(e)}, status=400)
  return JsonResponse({"error": "Invalid request method"}, status=405)

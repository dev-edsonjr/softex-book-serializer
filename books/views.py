from books.models import Book
from books.serializers import BookSerializer
from django.http import HttpResponse, JsonResponse

def book_list(request):
  if request.method  == 'GET':
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    
    return JsonResponse(serializer.data, safe = False)
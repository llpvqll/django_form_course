from django.shortcuts import render
from .models import Books, Author
from django.shortcuts import get_object_or_404
# Create your views here.


def base(request):
    template = 'base.html'
    books = Books.objects.order_by()
    author = Author.objects.order_by()
    context = {
        'books': books,
        'author': author,
    }

    return render(request, template, context)



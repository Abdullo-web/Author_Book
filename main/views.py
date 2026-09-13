from django.shortcuts import render, redirect
from .models import *

def main(request):
    return render(request, 'main.html')

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def author_create(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        b_date = request.POST.get('b_date')

        Author.objects.create(f_name=f_name,l_name=l_name,b_date=b_date)
        return redirect('authors')

    return render(request, 'author_create.html')

def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'author_detail.html', {'author': author})

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def book_create(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        pages = request.POST.get('pages')
        price = request.POST.get('price')
        description = request.POST.get('description')
        author_id = request.POST.get('author')
        author = Author.objects.get(id=author_id)

        Book.objects.create(title=title,author=author,pages=pages,price=price,description=description)
        return redirect('books')

    return render(request, 'book_create.html', {'authors': authors})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})

def book_update(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = Author.objects.get(id=request.POST.get('author'))
        book.pages = request.POST.get('pages')
        book.price = request.POST.get('price')
        book.description = request.POST.get('description')
        book.save()

        return redirect('books')

    return render(request, 'book_update.html', {'book': book, 'authors': authors})

def book_delete(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('books')

    return redirect('books')
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def books(request):
    book_list = [
        {'title': 'Harry Potter', 'pages': 350},
        {'title': 'The Hobbit', 'pages': 280},
        {'title': 'wripa biwis dgiuri', 'pages': 200},
        {'title': 'lord of the rings', 'pages': 500},
    ]
    return render(request, 'books.html', {'books': book_list})
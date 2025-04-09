from django.shortcuts import render
from .models import Book, Address
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg


# Create your views here.
def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def links(request):
 return render(request, "bookmodule/links.html")
def textformats(request):
 return render(request, "bookmodule/text/formatting.html")
def listing(request):
 return render(request, "bookmodule/listing.html")
def table(request):
 return render(request, "bookmodule/table.html")
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})
def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
    False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def list_q(request):
    mybooks=Book.objects.filter(Q(price__lte = 50))
    return render(request, 'bookmodule/queryQ.html', {'books':mybooks})
def list_q2(request):
    mybooks=Book.objects.filter(Q(edition__gt = 2) & (Q(title__contains = "qu") | Q(author__contains="qu") ))
    return render(request, 'bookmodule/queryQ.html', {'books':mybooks})
def list_q3(request):
    mybooks=Book.objects.filter(Q(edition__lte = 2) & ~(Q(title__contains = "qu") | Q(author__contains="qu") ))
    return render(request, 'bookmodule/queryQ.html', {'books':mybooks})
def list_q4(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodule/queryQ.html', {'books':mybooks})
def list_q5(request):
    total = Book.objects.count()
    mybooks=Book.objects.aggregate(total=Count('title'), sum=Sum('price', default=0), avg=Avg('price', default=0), max=Max('price', default=0), min=Min('price', default=0) )
    return render(request, 'bookmodule/queryQ5.html', {'books':mybooks})
def list_q6(request):
    Addresses=Address.objects.annotate(student_count=Count('student')).values('id','city', 'student_count')
    return render(request, 'bookmodule/queryQ6.html', {'address':Addresses})
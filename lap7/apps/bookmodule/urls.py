from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links', views.links, name="books.links"),
 path('html5/listing', views.listing, name="books.listing"),
 path('html5/table', views.table, name="books.table"),
 path('html5/text/formatting', views.textformats, name="books.text.formats"),
 path('simple/query', views.simple_query,name="books.allbooks"),
 path('complex/query', views.simple_query,name="books.allbooks"),
]

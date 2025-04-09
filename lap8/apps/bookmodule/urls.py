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
 path('lab8/task1', views.list_q,name="books.listQ"),
 path('lab8/task2', views.list_q2,name="books.listQ"),
 path('lab8/task3', views.list_q3,name="books.listQ"),
 path('lab8/task4', views.list_q4,name="books.listQ"),
 path('lab8/task5', views.list_q5,name="books.listQ"),
 path('lab8/task6', views.list_q6,name="books.listQ"),
]

from django.shortcuts import render
from .models import Book, Address
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg
from .models import Department, Student
from .models import Department
from .models import Course  # تأكد من أنك استوردت نموذج Course
from django.db import models 
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
    mybooks=Book.objects.filter(Q(price__lte = 80))
    return render(request, 'bookmodule/queryQ.html', {'books':mybooks})
def list_q2(request):
    mybooks=Book.objects.filter(Q(edition__gt = 3) & (Q(title__contains = "qu") | Q(author__contains="qu") ))
    return render(request, 'bookmodule/queryQ.html', {'books':mybooks})
def list_q3(request):
    mybooks=Book.objects.filter(Q(edition__lte = 3) & ~(Q(title__contains = "qu") | Q(author__contains="qu") ))
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
######################################################################
#def department_list(request):
 #   departments = Department.objects.all()
#  return render(request, 'bookmodule/department_list.html', {'departments': departments})
def task1(request):
    departments = Department.objects.all()  # الحصول على جميع الأقسام
    department_counts = []
    
    for department in departments:
        # حساب عدد الطلاب في كل قسم
        student_count = department.student_set.count()  # استخدام علاقة الـ ForeignKey لعد الطلاب
        department_counts.append({'department': department, 'student_count': student_count})

    return render(request, 'bookmodule/task1.html', {'department_counts': department_counts})  # تمرير البيانات إلى القالب



def task2(request):
    courses = Course.objects.all()  # جلب جميع الدورات
    course_counts = []

    # حساب عدد الطلاب المسجلين في كل دورة
    for course in courses:
        student_count = course.student_set.count()  # حساب عدد الطلاب المسجلين في الدورة
        course_counts.append({'course': course, 'student_count': student_count})

    return render(request, 'bookmodule/task2.html', {'course_counts': course_counts})


def task3(request):
    # استرجاع جميع الأقسام
    departments = Department.objects.all()
    oldest_students = []

    for department in departments:
        # ترتيب الطلاب في كل قسم حسب الـ ID من الأعلى (الأقدم) واختيار الطالب الأول
        oldest_student = department.student_set.order_by('-id').first()  # ترتيب تنازلي واختيار الطالب الأقدم
        if oldest_student:
            oldest_students.append({'department': department.name, 'oldest_student': oldest_student.name})

    return render(request, 'bookmodule/task3.html', {'oldest_students': oldest_students})


def task4(request):
    # استرجاع الأقسام التي تحتوي على أكثر من طالبين وترتيبها حسب عدد الطلاب بترتيب تنازلي
    departments = Department.objects.annotate(num_students=models.Count('student')).filter(num_students__gt=2).order_by('-num_students')
    
    return render(request, 'bookmodule/task4.html', {'departments': departments})








##########################################

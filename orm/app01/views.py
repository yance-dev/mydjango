from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from app01.models import Book


# Create your views here.

def index(request):
    # 方式一：
    # book_obj = Book(title="python_book",state=True,price=101,publish='机械工业出版社',pub_date='2018-08-17')
    # book_obj.save()
    # 方式2：
    book_obj = Book.objects.create(title="浪潮之巅", state=True, price=198, publish="科学出版社", pub_date="2018-12-12")
    print(book_obj.title)
    return HttpResponse('ojbk')


def bookstore(request):
    return HttpResponse('ok')


def addbook(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        Book.objects.create(title=title, price=price, pub_date=date, publish=publish, state=True)

        return redirect("app01:books")

    return render(request, 'addbook.html')


def books(request):
    booklist = Book.objects.all()

    return render(request, 'books.html', locals())


def delbook(request, id):
    Book.objects.filter(id=id).delete()
    return redirect("app01:books")


def modbook(request, id):
    book_obj = Book.objects.filter(id=id).first()

    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)

        return redirect("app01:books")

    return render(request, "modbook.html", {"book_obj": book_obj})

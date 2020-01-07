from django.shortcuts import render, redirect, HttpResponse
from app01.models import *


# Create your views here.
def add_book(request):
    """
    添加书籍信息的视图函数
    :param request:
    :return:
    """
    if request.POST:
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        authors = request.POST.getlist('authors')
        book_obj = Book.objects.create(title=title, price=price, pub_date=date, publish_id=publish)
        book_obj.authors.add(*authors)
        return redirect('app01:books')

    pub_list = Publish.objects.all()
    aut_list = Author.objects.all()

    return render(request, 'add_book.html', {'pub_list': pub_list, 'aut_list': aut_list})


def mod_book(request, id):
    mod_obj = Book.objects.filter(nid=id).first()
    if request.POST:
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        authors = request.POST.getlist('authors')
        Book.objects.filter(pk=id).update(title=title, price=price, pub_date=date, publish_id=publish)
        mod_obj.authors.set(authors)
        return redirect('app01:books')

    pub_list = Publish.objects.all()
    aut_list = Author.objects.all()
    return render(request, 'modbook.html', {'mod_obj': mod_obj, 'pub_list': pub_list, 'aut_list': aut_list})


def books(request):
    book_list = Book.objects.all()

    return render(request, 'books.html', {'book_list': book_list})


def del_book(request, id):
    Book.objects.filter(nid=id).delete()
    return redirect('app01:books')


def aut_detail(request, id, tag):
    if tag == "2":
        print(id)
        book_list = Book.objects.filter(authors__nid=id).all()
    else:
        book_list = Book.objects.filter(publish_id=id).all()
    return render(request, 'book_detail.html', locals())

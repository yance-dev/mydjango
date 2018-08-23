# -*- coding: utf-8 -*-
from django.urls import path, re_path, include
from app01 import views

app_name = 'app01'
urlpatterns = [
    re_path(r'^bookstore/', views.bookstore, name="bookstore"),
    re_path(r'^addbook/', views.addbook, name="addbook"),
    re_path(r'^books/', views.books, name="books"),
    re_path(r'app01/books/(\d+)/delete', views.delbook, name="del"),
    re_path(r'app01/books/(\d+)/modbook', views.modbook, name="mod"),

]

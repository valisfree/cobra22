#!/usr/bin/env python3 

# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        cobra22
# Created:     25.09.2018
# Version:     1.0
# Copyright:   (c) 2018, Vale_Phtor, valisfree@yandex.ru
# Licence:     Apache License version 2.0
#-------------------------------------------------------------------------------


import os.path
import re

def check_namefile(book):
    if re.findall(r'\.txt\b', book):
        return True
    return False
def check_file_existence(book):
    if not os.path.isfile(book):
        return False
    return True

def create_blank_file():
    """
    Создает пустой файл с базой данных.
    """
    if os.path.exists('books.kaa'):
        return
    else:
        stg_file = open("books.kaa", "w")
        stg_file.close()
        return
def list_of_books():
    """
    Читает файл с базой данных. Возвращает словарь книга:позиция,задержка
    """
    index_books = {}
    all_books = open("books.kaa", "r")
    for line in all_books:
        line = line.split("~")
        a = line[2]
        line[2] = a[0:-1]
        index_books[line[0]] = line[1], line[2]
    return index_books
def add_or_refresh_book(books, book):
    """
    Принимает словарь и список. Возвращает обновленный словарь с книгами.
    """
    if book[0] in books: # если книга есть в словаре
        if int(book[1]) <= int(books[book[0]][0]):
            return books
        books[book[0]] = book[1], book[2]
        return books
    else:
        books[book[0]] = book[1], book[2]
    return books
def open_and_create_book_list(book):
    '''
    Открывает и считывает данные из файла(книги).
    Возвращает список слов.
    '''
    book_list = []
    with open(book) as inf:
        for line in inf:
            line = line.strip()
            line = line.split()
            for str in line:
                book_list.append(str)
    return book_list
def save_to_file(books):
    """
    Записывает получаемый словарь в файл, удаляя старое содержимое.
    """
    f = open("books.kaa", "w")
    for i in books:
        f.write(i + "~" + str(books[i][0]) + "~" + str(books[i][1]) + "\n")
    f.close()
    return

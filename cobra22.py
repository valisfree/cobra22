#!/usr/bin/env python3 

# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        cobra22
# Created:     25.09.2018
# Version:     1.0
# Copyright:   (c) 2018, Vale_Phtor, valisfree@yandex.ru
# Licence:     Apache License version 2.0
#-------------------------------------------------------------------------------


# main
from stream import *
from processing import *
from communication import *

create_blank_file() # проверка наличия базы данных. если нет - создаем.
books = list_of_books() # создаем словарь книг
input_book = data_input() # получаем данные от пользователя
if not check_namefile(input_book[0]) or not check_file_existence(input_book[0]):
    no_file_or_not_txt()
    input_book = data_input() # получаем данные от пользователя
base_time = speed(input_book[2]) # вычисляем базовое время под заданную скорость
books = add_or_refresh_book(books, input_book) # обновляем словарь книг
words = open_and_create_book_list(input_book[0]) # получаем список слов
i = introductory_text() # вводный текст и пауза в ожидании начала.
# запускаем чтение
if i == '':
    stop = stream(words, books, input_book[0], int(books[input_book[0]][0]), base_time)
# чтение закончилось

books[input_book[0]] = stop, input_book[2] # сохраняем новую метку.
save_to_file(books) # сохраняем список книг в файл.
data_saved() # сообщаем, что данные сохранены.

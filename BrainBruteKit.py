# -*- coding: utf-8 -*-
__author__ = 'Mine_Bit'

import os
import sys
import time
import string

from BrainBrutekit.mod import popbrute
# Список TODO:
# 1. Добавить пробел после символов ">>" приведя к виду ">> " в функциях ввода информации с консоли

# Памятка  по значениям индексов:
# [0] - Gmail (@gmail.com)
#[1] - Yandex (@yandex.ru)
#[2] - Yandex (@ya.ru)
#[3] - Mail (@mail.ru)
#[4] - Mail (@inbox.ru)
#[5] - Mail (@list.ru)
#[6] - Mail (@bk.ru)
#[7] - Rambler (@lenta.ru)
#[8] - Rambler (@rambler.ru)
#[9] - Rambler (@autorambler.ru)
#[10] - Rambler (@myrambler.ru)
#[11] - Rambler (@ro.ru)
#[12] - Rambler (@r0.ru)
#[13] - Yahoo! (@yahoo.com)
#[14] - Microsoft (@outlook.com)
#[15] - Microsoft (@hotmail.com)
#[16] - Нераспознаное

# Создание переменных;


files_created = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False]
domain_list = (
    '@gmail.com', '@yandex.ru', '@ya.ru', '@mail.ru', '@inbox.ru', '@list.ru', '@bk.ru', '@lenta.ru', '@rambler.ru',
    '@autorambler.ru', '@myrambler.ru', '@ro.ru', '@r0.ru', '@yahoo.com', '@outlook.com', '@hotmail.com', None)

#Функция для упрощения вывода разделителя =)
def line_print():
    print('=========================================================================')


#Функция выполнения парсинга. Пришлось вывести в функцию, чтобы измерить время выполнения парсинга
def Search():
    out_file_names = (out_file + '_gmail.txt', out_file + '_yandex.txt', out_file + '_ya.txt', out_file + '_mail.txt',
                      out_file + '_inbox.txt', out_file + '_list.txt', out_file + '_bk.txt', out_file + '_lenta.txt',
                      out_file + '_rambler.txt', out_file + '_autorambler.txt', out_file + '_myrambler.txt',
                      out_file + '_ro.txt', out_file + '_r0.txt', out_file + '_yahoo.txt', out_file + '_outlook.txt',
                      out_file + '_hotmail.txt', out_file + '_else.txt')
    i = 0
    while i < len_of_f_list:
        c = 0
        for c in range(0, 16):
            if domain_list[c] in f_list[i]:
                if files_created[c] == False:
                    gmail_out_flie = open(out_file_names[c], 'w')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
                    files_created[c] = True
                else:
                    gmail_out_flie = open(out_file_names[c], 'a')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
            else:
                if files_created[16] == False:
                    gmail_out_flie = open(out_file_names[16], 'w')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
                    files_created[16] = True
                else:
                    gmail_out_flie = open(out_file_names[16], 'a')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
        i += 1
    print('Работа завршена!')


#Конец функции поиска

#Функция склейки файлов:
def Gluing():
    i = 0
    full_line_counter = 0
    while i < files_counter:
        try:
            f = open(array_file_names[i])
            f_list = f.readlines()
            len_of_f_list = len(f_list)
        except IOError:
            print("Файл не найден!")
        if len_of_f_list == 0:
            print('Файл для чтения пуст!')
        else:
            counter_lines = 0
            while counter_lines < len_of_f_list:
                append_out_file = open(output_file_name, 'a')
                append_out_file.write(f_list[counter_lines])
                append_out_file.close()
                full_line_counter = full_line_counter + 1
                counter_lines = counter_lines + 1
        i = i + 1


#Конец функции склейки

#Функция для генерации баз паролей:
def DicGenerate(ids_in, min_symb, max_symb, f_name, pass_amount):
    ABC = ''
    Alphs = {'1': string.ascii_uppercase, '2': string.ascii_lowercase, '3': string.digits, '4': string.punctuation}
    # Создание алфавита;
    for n in ids_in:
        ABC = ABC + Alphs[n]
    cpassout = ''
    p_num = 0
    f_num = 0
    f = open((f_name + str(f_num) + '.txt'), 'w')
    for curlength in range(min_symb, max_symb + 1):  # Перебор длин паролей в заданном диапазоне;
        password = []  # Обнуление пароля;
        for i in range(curlength):
            password.append(0)
            if p_num == pass_amount:  # Запись в новый файл при необходимости.
                f.close()
                f_num += 1
                f = open((f_name + str(f_num) + '.txt'), 'w')
                p_num = 0
        cpass = ''
        for i in password:
            cpass = cpass + ABC[i]
        f.write(cpass + '\n')
        p_num += 1
        contr = [len(ABC) - 1 for x in password]  # Создание контольного значения;
        while password != contr:  # Пока не закончатся комбинации;
            password[len(password) - 1] += 1  # Прибавление единицы в конец списка;
            if len(ABC) in password:  # Переход единицы на следующий уровень;
                j = len(password) - 1
                while len(ABC) in password:
                    password[j] = 0
                    password[j - 1] += 1
                    j += -1
            if p_num == pass_amount:  # Запись в новый файл при необходимости.
                f.close()
                f_num += 1
                f = open((f_name + str(f_num) + '.txt'), 'w')
                p_num = 0
            cpass = ''
            for i in password:
                cpass = cpass + ABC[i]
            f.write(cpass + '\n')
            p_num += 1
    f.close()
    print('Пароли сохранены в ' + f_name + '*_' + str(f_num) + '.txt')


#Конец функции генерации словарей

#Функция брутфорса:
#def Brutforse():
#Конец функции брутфорса

#Функция для старта парсинга:
def StartParse():
    line_print()
    print('Запушен модуль "Парсер" | Версия модуля: 0.4')
    line_print()
    file_to_parse = None
    out_file = None
    while True:
        print('Меню модуля "Парсер":')
        line_print()
        print('[0] - Просмотреть значения')
        print('[1] - Настроить значения')
        print('[2] - Запустить выполнение модуля')
        print('[777] - Выйти из модуля')
        line_print()
        input_int = int(input('>>'))
        line_print()
        if input_int == 0:
            print('Значения:')
            print('[0] - Файл для парсинга: ', file_to_parse)
            print('[1] - Основа имени файла для результата: ', out_file)
            line_print()
        elif input_int == 1:
            while True:
                print('Настройки значений:')
                print('[0] - Файл для парсинга | Текущее значение: ', file_to_parse)
                print('[1] - Основа имени файла для результата | Текущее значение: ', out_file)
                print('[777] - Выход из настроек')
                line_print()
                del input_int
                input_int = int(input('>>'))
                line_print()
                if input_int == 0:
                    print('Введите новое имя файла для парсинга:')
                    file_to_parse = str(input('>>'))
                    print('Новое значение присвоено!')
                    line_print()
                elif input_int == 1:
                    print('Введите основу имени файла для результата:')
                    print('!ВНИМАНИЕ! Данное значение не должно содержать расширение файла!')
                    out_file = str(input('>>'))
                    print('Новое значение присвоено!')
                    line_print()
                elif input_int == 777:
                    break
                else:
                    print('Ошибка ввода!')
                    line_print()
        elif input_int == 2:
            print('Проверяем значения:')
            try:
                f = open(file_to_parse)
                f_list = f.readlines()
                len_of_f_list = len(f_list)
            except IOError:
                print("Файл не найден!")
            if len_of_f_list == 0:
                print('Файл для чтения пуст!')
            else:
                file_size = os.path.getsize(file_name)
                line_print()
                print('Информация о входном файле:')
                print('Имя файла: ', file_to_parse)
                print('Количество аккаунтов: ', str(len_of_f_list))
                print('Обьем файла: ' + str(file_size) + ' байт')
                line_print()
                print('Информация о выходном файле:')
                print('Имя файла: ', out_file)
                line_print()
                print('Все значения проверены. Парсинг запущен!')
                start_time = time.time()
                Search()
                finish_time = time.time()
                line_print()
                print('Парсинг завершен!')
                print('Время выполнения: ', str(finish_time - start_time), ' сек')
                line_print()
        elif input_int == 777:
            print('Выход из модуля "Парсинг"...')
            break
        else:
            print('Ошибка ввода!')
            line_print


#Конец функции для старта парсинга

#Функция для старта склейки:
def StartGluing():
    files_counter = 0
    array_file_names = []
    output_file_name = None
    print('Запушен модуль "Склейщик" | Версия модуля: 0.2')
    while True:
        line_print()
        print('Меню модуля "Склейщик":')
        print('[0] - Просмотреть значения')
        print('[1] - Настроить значения')
        print('[2] - Запустить выполнение модуля')
        print('[777] - Выйти из модуля')
        line_print()
        del input_int
        input_int = int(input('>>'))
        line_print()
        if input_int == 0:
            print('Значения:')
            print('[0] - Файлы для склейки:')
            print(array_file_names)
            print('[1] - Имя файла результата: ', output_file_name)
            line_print()
        elif input_int == 1:
            while True:
                print('Настройка значений:')
                print('[0] - Файлы для склейки | Текущее количество: ', files_counter)
                print('[1] - Имя файла результата | Текущее значение: ', output_file_name)
                print('[777] - Выход из настроек')
                line_print()
                del input_int
                input_int = int(input('>>'))
                line_print()
                if input_int == 0:
                    while True:
                        print('Введите количество файлов для склейки:')
                        files_counter = int(input('>> '))
                        if files_counter <= 1:
                            print('Введенно неверное значение!')
                        else:
                            break
                    print('Вводите имена файлов построчно:')
                    i = 0
                    while i < files_counter:
                        while True:
                            input_file_name = str(input('>> '))
                            if len(input_file_name) != 0:
                                array_file_names.append(input_file_name)
                                break
                            else:
                                print('Ошибка ввода! Повторите операцию!')
                        i = i + 1
                    del i
                    print('Значения успешно присвоенны!')
                    line_print()
                elif input_int == 1:
                    while True:
                        print('Введите имя выходного файла:')
                        output_file_name = str(input('>> '))
                        if len(output_file_name) != 0:
                            break
                        else:
                            print('Ошибка ввода! Повторите операцию!')
                    output_file = open(output_file_name, 'w')
                    output_file.write('Склеено с помощью BrainBruteKit 0.1 by brainhands.ru \n')
                    output_file.close()
                    print('Значения успешно присвоенны!')
                    line_print()
                elif input_int == 777:
                    break
                else:
                    print('Ошибка ввода!')
                    line_print()
        elif input_int == 2:
            print('Начинаем склейку...')
            start_time = time.time()
            Gluing()
            finish_time = time.time()
            line_print()
            print('Работа модуля "Склейка" завершен!')
            print('Время выполнения: ', str(finish_time - start_time), ' сек')
            line_print()
        elif input_int == 777:
            print('Выход из модуля "Склейка"...')
            break


#Конец функции для старта склейки

#Функция для старта генератора:
def StartGenerate():
    IDs = '1'
    min_symb = 0
    max_symb = 0
    f_name = None
    pass_amount = 100000
    line_print()
    print('Запущен модуль "Генератор Словарей" | Версия модуля: 0.3')
    line_print()
    while True:
        print('Меню модуля "Генератор Словарей":')
        line_print()
        print('[0] - Просмотреть значения')
        print('[1] - Настроить значения')
        print('[2] - Запустить выполнение модуля')
        print('[777] - Выйти из модуля')
        line_print()
        input_int = int(input('>> '))
        line_print()
        if input_int == 0:
            print('Значения:')
            print('[0] - Наборы символов: ', IDs)
            print('[1] - Минимальная длина пароля: ', min_symb)
            print('[2] - Максимальная длина пароля: ', max_symb)
            print('[3] - Название словаря: ', f_name)
            print('[4] - Количество паролей в каждой части словаря: ', pass_amount)
            line_print()
        elif input_int == 1:
            while True:
                print('Настроки значений:')
                print('[0] - Наборы символов | Текущее значение: ', IDs)
                print('[1] - Минимальная длина пароля | Текущее значение: ', min_symb)
                print('[2] - Максимальная длина пароля | Текущее значение: ', max_symb)
                print('[3] - Название словаря | Текущее значение: ', f_name)
                print('[4] - Количество паролей в каждой части словаря | Текущее значение: ', pass_amount)
                print('[777] - Выход из настроек')
                line_print()
                input_int = int(input('>> '))
                line_print()
                if input_int == 0:
                    print('Введите подряд номера наборов символов:')
                    print('[1] - EN (большие)')
                    print('[2] - en (маленькие)')
                    print('[3] - Цифры')
                    print('[4] - Пунктуационные знаки')
                    IDs = input('>> ')
                    line_print()
                elif input_int == 1:
                    print('Задайте минимальное количество символов в паролях:')
                    min_symb = int(input('>> '))
                    line_print()
                elif input_int == 2:
                    print('Задайте максимальное количество символов в паролях:')
                    max_symb = int(input('>> '))
                    line_print()
                elif input_int == 3:
                    print('Назовите получаемый словарь:')
                    f_name = input('>> ')
                    line_print()
                elif input_int == 4:
                    print('Введите количество паролей в каждой части словаря:')
                    pass_amount = int(input('>> '))
                    line_print()
                elif input_int == 777:
                    break
                else:
                    print('Ошибка ввода!')
        elif input_int == 2:
            start_time = time.time()
            DicGenerate(IDs, min_symb, max_symb, f_name, pass_amount)
            finish_time = time.time()
            line_print()
            print('Работа модуля "Генератор Словарей" завершена!')
            print('Время выполнения: ', str(finish_time - start_time), ' сек')
            line_print()
        elif input_int == 777:
            print('Выход из модуля "Генератор Словарей"...')
            break

        else:
            print('Ошибка ввода!')
#Конец функции для старта генератора


def StartBrutforse():
    line_print()
    print('Запущен модуль "Брутфорс" | Версия модуля: 0.2')
    line_print()
    while True:
        print('Меню модуля "Брутфорс":')
        line_print()
        print('[0] - POP Брутфорс')
        print('[1] - FTP Брутфорс')
        print('[2] - Gmail Брутфорс')
        print('[3] - IMAP Брутфорс')
        print('[4] - MySQL Брутфорс')
        print('[5] - NNTP Брутфорс')
        print('[6] - SMTP Брутфорс')
        print('[7] - SSH Брутфорс')
        print('[8] - Telnet Брутфорс')
        print('[777] - Выход')
        line_print()
        read_line = int(input('>> '))
        line_print()
        if read_line == 0:
            while True:
                server_in = None
                userlist_in = None
                wordlist_in = None
                print('Модуль "POP Брутфорс" | Версия модуля: 0.2 ')
                line_print()
                print('Меню модуля "POP Брутфорс":')
                line_print()
                print('[0] - Просмотреть значения')
                print('[1] - Изменить значения')
                print('[2] - Запустить модуль')
                print('[777] - Выйти из модуля')
                line_print()
                read_line = int(input('>> '))
                line_print()
                if read_line == 0:
                    print('Значения:')
                    print('[0] - Адрес сервера : ',server_in)
                    print('[1] - Файл с логинами: ',userlist_in)
                    print(('[2] - Файл с словарем: ',wordlist_in))
                elif read_line == 1:
                    while True:
                        print('Изменить значения:')
                        print('[0] - Адрес сервера | Текущее значение: ',server_in)
                        print('[1] - Файл с логинами | Текущее значение: ',userlist_in)
                        print(('[2] - Файл с словарем | Текущее значение: ',wordlist_in))
                        print('[777] - Выход')
                        read_line = int(input('>> '))
                        if read_line == 0:
                            line_print()
                            print('Введите новое значение "Адрес сервера":')
                            server_in = input('>> ')
                            line_print()
                        elif read_line == 1:
                            line_print()
                            print('Введите новое значение "Файл с логинами":')
                            userlist_in = input('>> ')
                            line_print()
                        elif read_line == 2:
                            line_print()
                            print('Введите новое значение "Файл с словарем":')
                            wordlist_in = input('>> ')
                            line_print()
                        elif read_line == 777:
                            break
                        else:
                            line_print()
                            print('Ошибка! Введено неверное значение!')
                elif read_line == 2:
                    print('Проверка значений...')
                    if server_in != None | userlist_in != None | wordlist_in != None:
                        print('Значения не равны нулю...')
                        print('Запуск модуля...')
                        start_time = time.time()
                        popbrute.Strart(server_in,userlist_in,wordlist_in)
                        finish_time = time.time()
                        line_print()
                        print('Работа модуля "POP Брутфорс" завершена!')
                        print('Время выполнения: ', str(finish_time - start_time), ' сек')
                        line_print()
                    else:
                        line_print()
                        print('Значения пусты!')
                        line_print()
                elif read_line == 777:
                    print('Выход из модуля "POP Брутфорс"...')
                    line_print()
                    break
                else:
                    print('Ошибка! Введено неверное значение!')
                    line_print()



def StartCheck():
    pass0


def Help():
    pass


def Info():
    pass


def Exit():
    sys.exit(1)


#Начало работы скрипта:
print()
line_print()
print('BrainBruteKit | 0.1 | By Mine_Bit')
print('Coded By Mine_Bit [Brain Hands]')
print('Официальный сайт: brainhands.ru')
line_print()
while True:
    print('Главное меню:')
    line_print()
    while True:
        print('Выберите функцию:')
        print('[0] - Парсер')
        print('[1] - Склейщик баз')
        print('[2] - Генератор словарей')
        print('[3] - Брутфорс')
        print('[4] - Чеккер')
        print('[99] - Помощь')
        print('[100] - Информация')
        print('[777] - Выход')
        line_print()
        input_int = int(input('>>'))
        line_print()
        if input_int == 0:
            StartParse()
            break
        elif input_int == 1:
            StartGluing()
            break
        elif input_int == 2:
            StartGenerate()
            break
        elif input_int == 3:
            StartBrutforse()
            break
        elif input_int == 4:
            StartCheck()
            break
        elif input_int == 99:
            Help()
            break
        elif input_int == 100:
            Info()
            break
        elif input_int == 777:
            Exit()
        else:
            print('Введено неверное значение!')
            #Конец работы скрипта

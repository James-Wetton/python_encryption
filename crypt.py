import math
import pybase64
from string import ascii_lowercase
from collections import Counter
import time
import os
import sys
import codecs


mode = False
while True:
    askmode = str(input("type encrypt to type a new message in, type decrypt to solve an existing message: "))
    #askey = str(input("insert key: "))
    if askmode == "encrypt":
        enterpass = str(input("message: "))
        encodedpass = enterpass.encode('utf-8')
        cr = pybase64.standard_b64encode(encodedpass)
        cr = cr.decode('utf-8')
        cr = codecs.encode(cr)
        print(cr)
    if askmode == "decrypt":
        enterpass = str(input("message: "))
        enterpass = codecs.decode(cr)
        enterpass = pybase64.standard_b64decode(enterpass)
        enterpass = str(enterpass)
        enterpass = enterpass[2:]
        enterpass = enterpass[:-1]
        #enterpass = enterpass + str(askey*9)
        print(enterpass)
        #enterpass = " "


    

 
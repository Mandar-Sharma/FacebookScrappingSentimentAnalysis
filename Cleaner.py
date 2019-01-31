#!/usr/bin/python
# -*- coding: utf-8 -*-
from googletrans import Translator
import csv
import string
import sys
import json
import pickle

reload(sys)
sys.setdefaultencoding('utf8')
translator = Translator()

#To filter for characters
printable = set(string.printable)
#filter(lambda x: x in printable, s)

path = "C:\Users\Mandar PC\Desktop\NLP\Alliance"
db1= open(path+'\\FireSideYT.csv','rb')
total = open(path+'\FireSideYTCleaned.json','wb')
db1read = csv.reader(db1)

#Facebook: 3:Comment 4: Author 5:Published Date 6:Reactions 7:Likes 8:Loves 9:Wows 10:Hahas 11:Sads 12:Angrys 13:Special
#Youtube: 2:Date 3: Timestamp 4:Comment 5:likes 6:Has reply? 7:Number of replies
count = 0
for row in db1read:
    delist=[]
    jpt = row[4]
    try:
        undr = translator.translate(jpt,dest='en')
        dr = undr.text
        delist.extend((filter(lambda x: x in printable, dr),filter(lambda x: x in printable, row[5]),filter(lambda x: x in printable,row[6]),
            filter(lambda x: x in printable, row[7]))) 
        json.dump(delist, total, indent=2)
        print ('Done with: ',count)
        count = count + 1
        #wr.writerow(delist)
     
    except Exception as e:
        print 'Err'
        
    


#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
import os
import re

os.system("clear")
last=os.popen("last")
line_last=last.readlines()


#-----------------Liste-----------------------------
login=[]
date=[]
nombre_heure=[]
nombre=[]
#------------------Parsage document-----------------
pattern="^[a-zA-Z0-9_]+[ \t]"#expression pour récupérer le login
date1="[A-Z].{2}\s{1,2}[0-9]{1,2}"
heure="[0-9]{2}:[0-9]{2}"
for line in line_last:
    
    login.append(re.findall(pattern,line))#Ajout login>liste_login
    date.append(re.findall(date1,line))
    nombre_heure.append(re.findall(heure,line))
print login
print date
print nombre_heure



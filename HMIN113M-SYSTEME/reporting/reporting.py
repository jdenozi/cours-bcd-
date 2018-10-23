#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
import os
import re

os.system("clear")
popen=os.popen("last")
last=popen.readlines()

liste_login=[]
date=[]
#-----------------Dictionnaire----------------------------
dic={}
dic_heure={}
dic_date={}
#------------------Parsage document-----------------

#Pattern expression reguliere
pattern_log="^[a-zA-Z0-9_]+[ \t]"#récupérer le login
pattern_date="[A-Z].{2}\s{1,2}[0-9]{1,2}"#récupérer la date
pattern_heure="\S\d{2}:\d{2}\S"#récupérer l'heure


for line in last:
    #Etape de création du dictionnaire avec login et nombre de connexion
    login=re.sub("\W","", str(re.findall(pattern_log,line)))
    if login in dic:
        dic[login]=dic.get(login)+1
    else:
        dic[login]=1
    #Etape de création du dictionnaire avec login et temps de connexion par login
    temps=re.sub("\W","",str(re.findall(pattern_heure,line)))
    minute=re.sub("^\d{2}","",temps)
    heure=re.sub("\d{2}$","",temps)
    date_line=str(re.findall(pattern_date,line))
    
    for i in dic:
        if i==login:
            if temps is not "":
                if i not in dic_heure:
                    dic_heure[date_line]=((int(heure)*60)+int(minute))
                    
                else:
                    dic_heure[date_line]=dic.get(date)+((int(heure)*60)+int(minute))
            else:
                break
    #Etape de création du dictionnaire  avec key de login et date donnant le temps de connexion
    #date_line=str(re.findall(pattern_date,line))
    for j in dic_heure:
        if date_line==j:
            dic_date[login]=dic_heure
            
        else:
            break



def loginConnexion(login):
    print login,"s'est connecté ", dic.get(login),"fois"
    
def tempsConnexion(login):
    print "les connexions en fonction des dates sont de ",login,dic_date.get(login)

def tempsConnexionDate(login,date):
    print "la connexion du ",date,"de",login,dic_date.get(login).get(date)

#loginConnexion("denozi")
#tempsConnexion("denozi")
tempsConnexionDate("denozi","['Oct 10']")
# 　　　　　　　　　　　　　　　　　　 ﾍ
#　　　　　　　　　　　　　　 ﾍ　　　/　|
#　　　　　　　　　　　　　 / ｜　 /　　|
#　　　　　　　　　    　 ﾉ　　|　ﾉ 　 　|
#　　      　　　　　　　ﾉ　　ヽﾐ}　F′　 ｯ┘
#　  　 　    　　　　　{^^ . -┴┴‐ミ   　　ﾐ.._
#　  　 　　　　　　> ´　　　　　　　    　ミ､
#　　　　　　　 　/　　　　　　　　　　　    ﾐ､
#　　　　　　　  ﾉ　　p￣ヽ_　　　　　　     　ﾐ､
#　　　　　rﾍ⌒　　    `ー ′　　　　　　　       ﾐ､
#　　　　ﾆ{^　　　　　　　　　　　　　　　      ﾐ､
#　　　　 〈､_　　　＝三二_ー--　　　　　       l
#　　　　∠_　　　　　ｰ＝= 二_ｰ
#　 　／　　 ¨ヾ､
#　 ﾉﾍ　　　　　　ヽ JulienDenozi

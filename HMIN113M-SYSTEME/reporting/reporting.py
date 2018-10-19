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
    #Etape 
    temps=re.sub("\W","",str(re.findall(pattern_heure,line)))
    minute=re.sub("^\d{2}","",temps)
    heure=re.sub("\d{2}$","",temps)
    
    for i in dic:
        if i==login:
            if temps is not "":
                if i not in dic_heure:
                    dic_heure[login]=((int(heure)*60)+int(minute))
                else:
                    dic_heure[login]=dic.get(login)+((int(heure)*60)+int(minute))
            else:
                break
                        

print dic_heure            
        


#for line in line_last:
#    print line
#    login=re.sub("\W","", str(re.findall(pattern_log,line)))

#    if login not in liste_login:
#        liste_login.append(login)
#    else:
#        break

#    date.append(re.findall(pattern_date,line))
#    heure=re.sub("\W","",str(re.findall(pattern_heure,line)))
#    minute=re.sub("^\d{2}","",heure)
#    heure_minute=re.sub("\d{2}$","",heure)
    
#    print heure
#    if heure:
#        heure1=(int(re.sub("\W","",heure))/60)+heure_minute
#    else:
#        heure1="none"
#        if dic_heure.get(login):
#            dic_heure[login]=dic_heure.get(login)+heure1
#        else:
#           dic_heure[login]=heure1
    
#    dic[login] =len(date)
#    for keys in dic:
#        if keys not in liste_login:
#            liste_login.append(keys)
#
#print dic_heure
#print dic
#print liste_login
def loginConnexion(login):
    print login,"s'est connecté ", dic.get(login),"fois"
    
def tempsConnexion(login):
    print login, "s'est connecté", dic_heure.get(login),"minutes"

loginConnexion("denozi")
tempsConnexion("denozi")
# 　　　　　　　　　　　　　　　　　　 ﾍ
#　　　　　　　　　　　　　　 ﾍ　　　/　|
#　　　　　　　　　　　　　 / ｜　 /　　|
#　　　　　　　　　 }YL　 ﾉ　　|　ﾉ 　 　|
#　　　　　　　　　ﾉ　　ヽﾐ}　F′〉　 ｯ┘
#　 　 　　　　　　{^^ . -┴┴‐ミ　　ﾐ.._
#　 　 　　　　　　> ´　　　　　　　　ミ､
#　　　　　　　 　/　　　　　　　　　　　 ﾐ､
#　　　　　　　  ﾉ　　p￣ヽ_　　　　　　 　ﾐ､
#　　　　　rﾍ⌒　　    `ー ′　　　　　　　   ﾐ､
#　　　　ﾆ{^　　　　　　　　　　　　　　　  ﾐ､
#　　　　 〈､_　　　＝三二_ー--　　　　　    l
#　　　　∠_　　　　　ｰ＝= 二_ｰ
#　 　／　　 ¨ヾ､
#　 ﾉﾍ　　　　　　ヽ JulienDenozi

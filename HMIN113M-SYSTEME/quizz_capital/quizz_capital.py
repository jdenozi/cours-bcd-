#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
#QUIZZ CAPITALE#
import csv
import random

with open('capitales.csv','r') as csvfile:
    capitale_pays=csv.reader(csvfile)
    pays=[]
    capitale=[]
    for i in capitale_pays:
        pays.append(i[0])
        capitale.append(i[1])
parse=[]
for i in pays:   
    parser= i.split(" (")
    parse.append(parser)

#Parsage du determinant
determinant_pays=[]
pays_sans_determinant=[]
for i in parse:
    pays_seul=i[0]
    pays_sans_determinant.append(pays_seul)
    if len(i)>1:
        determinant= i[1]
        determinant_without_last_char=determinant.replace(")","")
        determinant_pays.append(determinant_without_last_char)
    else:
        determinant_pays.append("")
print "**************BIENVENUE DANS L'INCROYABLE QUIZZ DES CAPITALES******************"

print "Combien de question voulez vous ?"
bonne_reponse=0
a=raw_input()        
for i in range(int(a)):
    indice= random.randrange(len(pays))
    print "Quel est la capitale de "+determinant_pays[indice]+" "+ pays_sans_determinant[indice]
    print "Ecris ta reponse"
    reponse=raw_input()
    if reponse==capitale[indice]:
        print "Tu es genial mon pote"
        bonne_reponse=bonne_reponse+1
        
    if reponse!=capitale[indice]:
        print "Tu pue le chibre, la réponse était "+ capitale[indice]
print "Le quizz est terminé, je sais que c'était le feu, mais toute bonne chose à un fin"
ratio=(bonne_reponse*100)/int(a)
print "Tu as eu "+str(ratio)+"% de  bonne reponse"

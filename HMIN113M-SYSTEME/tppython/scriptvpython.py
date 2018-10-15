#!/usr/bin/env python2.7
import sys

#
#print("hello world")

#if len(sys.argv)== 0:
	#print("non")
#else :
	#print("oui")


#for i in sys.argv:
#	print i[1:]

#def f(n):
	#if n<2:
#		return 1
	#else:
 #		return n*f(n-1)
#print f(5)#


n=int(sys.argv[1])
listenp=[2]

for i in range(2,n): #liste dont je veux avoir si c'est un nb premier
	premier=0
 	for j in listenp:
 		if i%j==0:
 			premier=1
 			break
 	if premier==0:
 		listenp.append(i)
print listenp

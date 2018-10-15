somme<-0
for (i in 1:100){somme=somme+i}
print(somme)

eq<- function(a,b,c){
	x1<- 0
	x<-0
	x2 <-0
	d<-(b*b)-(4*a*c)

	cat("le delta de l'équation est égale à", d )
	if (d<0){
		print("Il n'y a pas de solution")
	}
	if (d==0){
		x<--b/(2*a)
	       	print (x)
	}
	if(d>0) {
		print("Les deux solutions sont : \n ")
	        x1<-((-b-sqrt(d))/(2*a)) 
	       	print (x1)
		x2<-((-b+sqrt(d))/(2*a)) 
	       	print (x2)	
	}
}
eq(2,-1,-6)

monvec=c(1,5,8,23,4,90,12)
print(monvec)
grosvec=1:300
print(grosvec)

print (sum(1:100))
vect=c(27,32,56,78,11,45)
vect
print(vect[c(2,4)])
print(vect[1:3])
print(vect[vect>40])

print (min(vect))
print(max(vect))
print(sort(vect))
print(rank(vect))
print (order(vect))

print (1[order(2)])

semaine=1:7
jours=c("lundi","mardi"," mercredi", "jeudi", "vendredi","samedi","dimanche")
for(i in semaine)for (j in jours)
	names(semaine)<-jours
print(semaine)

#excercice 19- FONCTION MOYENNE
moyenne<-function(a){
	num<-0
	moy<-0
	sum<-0
	for (i in a){
		sum=i+sum
		num=num+1
	}
moy<-sum/num	
print(moy)
}
moyenne(vect)
print(vect

#excercice 19- FONCTION ECART TYPE
moyenne<-function(a){
        num<-0
        moy<-0
        sum<-0
        for (i in a){
                sum=i+sum
                num=num+1
        }
moy<-sum/num
print(moy)
}


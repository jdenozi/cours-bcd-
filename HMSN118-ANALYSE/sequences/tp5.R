library(ape)
align<-read.dna("BCRA1.out", format="fasta", as.character=TRUE)
BRCA1<-read.dna("BRCA1.fasta", format="fasta")


calcul_gap<-function(x){
	nombre_gap<-0
	liste_gap<-c()
	compteur<-0

	for(i in x){
		if(i=="-"){
		    compteur=compteur+1
		    }
		else{
			if(compteur>0){
			    nombre_gap<-nombre_gap+1
			    liste_gap<-c(liste_gap,compteur)
			    compteur=0  
			    }
		}
		    
		}
	print(liste_gap)
	print(nombre_gap)
}
calcul_gap(align[1,])
calcul_gap(align[7,])
print(BCRA1)
print(dist.dna(BRCA1))

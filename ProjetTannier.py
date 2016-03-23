### LIBRARY IMPORTEES ###
from string import *
from csv import *




######################################################################################
##  LECTURE DU FICHIER ET RECUPERATION DE LA TAILLE ET DU NOMBRE DE SITE INDEFINIS  ##
######################################################################################

def readFasta(file):
      "This function read one sequence in a fasta file and returns two strings"
      infile=open(file, 'r')
      seq=""
      name = ""
      taille = 0
      taille2 = 0
      nbreN = 0
      tmp=infile.readlines()
      infile.close()
      name =tmp[0][1:-1] # pour eliminer le > du debut et le \n de fin
      for x in tmp[1:] : # On recupere le nombre  de site indefinis dans le fichier
            for i in x:
                  taille +=1 # On compte le nombre de caracteres et donc de nucleotides 
                  if i == "N" :
                        nbreN +=1

            seq=seq+upper(x[:-1]) #upper passe les caracteres en majuscule
      return name,seq ,taille,nbreN # la fonction retourne le nom et la sequence


##########################################################################################
##                  LECTURE DU FICHIER CSV ET FILTRAGE DES DONNES                       ##
##########################################################################################

def readCsv(file):
      "This function read csv file"
      infile = open(file,'r')
      tmp = infile.readlines()
      infile.close()
      name = tmp[0]
      alignement = []
      for x in tmp[1:]:
            alignement.append(x)
      print name 
      print alignement[0]




      

######################################################################################
##                                      MAIN                                        ##
######################################################################################

## Determination de la taille du genome et du nombre de N 

Ancestral = readFasta("GenomeAncestral.txt")
tailleGenomeAncestral = Ancestral[2]
print "La taille du genome Ancestral est : " , tailleGenomeAncestral
nbreDeNAncestral = Ancestral[3]
print "Il y a ", nbreDeNAncestral,"N dans le genomeAncestral"

Actual = readFasta("SequenceActuel.txt")
tailleGenomeActuel = Actual[2]
print "La taille du genome Actuel est : " , tailleGenomeActuel
nbreDeNActuel = Actual[3]
print "Il y a ", nbreDeNActuel,"N dans le genomeActuel"

## Determination des orthologues

Csv = readCsv("AlignementTable.csv")





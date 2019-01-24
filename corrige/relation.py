#!/usr/bin/env python3
from anneau01 import *

###########################################################################################
# The following functions create the random, the empry and the full relations, respectively 
###########################################################################################

def genR(A,B):
    r = []
    for i in range(A):
        l = []
        for j in range(B):
            l.append(randint(0,1))
        r.append(l)
    return r

def genVide(A, B):
	r = []
	for i in range(A):
		l = []
		for j in range(B):
			l.append(zero())
		r.append(l)
	return r

def genPleine(A, B):
	r = []
	for i in range(A):
		l = []
		for j in range(B):
			l.append(unit())
		r.append(l)
	return r


#####################################################################################
#### FUNCTION AFFICHE ###############################################################

#### (optional)
#### When creating a matrix as a list of lists, and printing it with print(), it is not displayed in the shape of a matrix
#### Then this function print the object in a shape of a matrix
def imprimeTableau(R):
	for i in range(len(R)):
		print(R[i])
	print("\n")

##### When we pass an argument to a function, we create a reference to this object.
##### So, when replacing its values inside of the function we are also modifying the original matrix
##### For this reason, we create a new table inside of the function,
##### which receives "*" in the positions where R contains 1 and " " where R contains 0
def affiche(R):
	S = []
	for i in range(len(R)):
		l = []
		for j in range(len(R[i])):
			if R[i][j] == unit():
				l.append("*")
			else:
				l.append(" ")
		S.append(l)

	print("\nAffiche: ")
	imprimeTableau(S)


###################################################################################
### The predicates

def successeur(i,j):
	if i == j + 1:
		return unit()
	return zero()

def moitie(i,j):
	if i == j // 2:
		return unit()
	return zero()

def diviseurNonTrivial(i,j):
	l = [1, j]
	if j == 0:
		return zero()
	if (i % j) == 0 and i not in l:
		return unit()
	return zero()


##################################################################################
### FONCTION CONVERSION ##########################################################
### The getFunction() function supports the conversion function returning the concerning predicate 
### It is called inside conversion as the condition to fill the relation
#################################################################################

def getFunction(p, i, j):
	if p == "successeur":
		return successeur(i,j)
	elif p == "moitie":
		return moitie(i,j)
	elif p == "diviseur":
		return diviseurNonTrivial(i,j)

def conversion(p, a, b):
	r = []
	for i in range(a):
		l = []
		for j in range(b):
			l.append(getFunction(p, i, j))
		r.append(l) 
	return r


##############################################################
### symetrie function

def symetrie(R):
	S = []
	for i in range(len(R)):
		l = []
		for j in range(len(R[i])):
			l.append(R[j][i])
		S.append(l)
	return S


#############################################################
# composition function
def composition(S, R):
	r = []
	for a in range(len(R)):
		l = []
		for c in range(len(R[a])):
			value = 0
			for b in range(len(S[a])):
				value = somme(value, produit(R[a][b], S[b][c]))
			l.append(value)
		r.append(l)
	return r

def inclus(R, S):
	for i in range(len(R)):
		for j in range(len(R[i])):
			if R[i][j] != S[i][j]:
				return False
	return True


def main():
	# display (affiche) exercise
	R = genVide(2, 3)
	affiche(R)

	R = genPleine(4, 5)
	affiche(R)

	# predicate exercise
	print ("successeur: ")
	affiche(conversion("successeur", 3, 3))
	print ("moitie: ")
	affiche(conversion("moitie", 3, 3))
	print ("diviseur:")
	affiche(conversion("diviseur", 6, 6))

	# symmetrie exercise
	R = conversion("successeur", 3, 3)
	print("R:")
	imprimeTableau(R)

	S = symetrie(R)
	affiche(S)

	#composition exercise
	R = composition(R, R)
	affiche(R)

	S1 = composition(S, S)
	print ("S1:")
	imprimeTableau(S1)

	#union and intersection exercise
	print ("union S and S1: ")
	imprimeTableau(union(S, S1))
	print ("intersection R and S1: ")
	imprimeTableau(intersection(R, S1))

	# inclusion exercise
	S2 = composition(S, S1)
	print ("S2: ")
	imprimeTableau(S2)

	S1uS2 = union(S1, S2)
	print ("S1ouS2:")
	imprimeTableau (S1uS2)

	print(inclus(S1, S2))
	print(inclus(S1, S1uS2))
	#print inclus(genVide(2,2), genPleine(2,2))
	print(inclus(conversion("moitie", 3, 3), conversion("diviseur", 6, 6)))

    
if __name__ == "__main__":
    main()

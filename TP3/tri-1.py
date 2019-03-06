#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from random import randint
from scipy import *


#########################################################################
# Génération d’une séquence de nombres entiers aléatoires
#########################################################################
def gen_seq_aleat(taille, valeur_min, valeur_max):
    """ Génération d’une séquence de nombres entiers aléatoires

    :param taille: taille de la séquence à générer
    :param valeur_min: valeur minimal des nombres entiers générés
    :param valeur_max: valeur maximal des nombres entiers générés
    :return séquence générée: liste dont les éléments sont
    des triplets [indice courant, indice initial, valeur]
    """
    # Les éléments de "seq" sont des triplets [indice courant, indice initial, valeur]
    # L'indice initial est l'emplacement de l'élement dans la séquence au moment de la génération
    # L'indice courant sera l'indice une fois l'élément trié
    seq = []
    print("\n *** gen_seq_aleat: paramètres de la génération pseudo-aléatoire =",
          [taille, valeur_min, valeur_max])
    l = []
    # Géneration de la séquence
    ... # A COMPLETER
    return seq


##########################################################################
# tri par insertion
##########################################################################
def tri_insertion(seq):
    """ Trie la séquence en paramètre dans le sens croissant.

    :param seq: séquence sur laquelle le tri est effectué
    """
    ... # A COMPLETER



if __name__ == "__main__":

    ####################################################
    # Tests de génération aléatoire de séquences à trier
    ####################################################
    print("\n Tests de génération aléatoire de séquences à trier",
          " triplets avec valeurs en 3 composant) \n\n")
    # Generer et afficher seq1, seq2 et seq3
    seq1 = ... # COMPLETER
    seq2 = ... # COMPLETER
    seq3 = ... # COMPLETER
    print("\n *** Seq1 = \n", array(seq1), "\n")
    print("\n *** Seq2 = \n", array(seq2), "\n")
    print("\n *** Seq3 = \n", array(seq3), "\n")

    #######################################################
    # Tests du tri par insertion sur des données aléatoires
    #######################################################
    print("\n Tests du tri par insertion sur des données aléatoires \n\n")
    print("\n ************** \n *** Test 1 ***\n ************** ")
    # Affichage avant le tri
    print(" *** Seq1 = \n", array(seq1), "\n")
    # Tri 
    ... # A COMPLETER
    # Affichage après le tri
    print(" *** Tri1 = \n", array(seq1), "\n")
    print("\n ************** \n *** Test 2 ***\n ************** ")
    ... # A COMPLETER
    print("\n ************** \n *** Test 3 ***\n ************** ")
    ... # A COMPLETER

#Header
"""
ce programme permet de jouer au pendu .
Vous avez 8 essais pour découvrir le mot
Auteur: Joris CLEMENT.
date de réalisation: 23/11/2020
"""

#Importation des bibliothéques
import random


#Fonction nécessaires au programme

from TP2_lib import randomWord,afficher,jouer



#Programme principal


essai = 0
mot = randomWord()

motFinal=(afficher(mot))
print (motFinal)
print(jouer(essai,mot,motFinal))


#@Copyright: Joris CLEMENT
#Header
"""
ce programme permet de jouer au pendu .
Vous avez 8 essais pour découvrir le mot
Auteur: Joris CLEMENT.
date de réalisation: 23/11/2020
"""
"""
TODO changer le noms des variables et fonction pour tout mettre en anglais.
     faire une sécurtité de saisie
     un compteur de point 
"""

#Importation des bibliothéques
import random

#Fonction nécessaires au programme

from TP2_lib import randomWord,afficher,jouer,winLose,jouerAffichage



#Programme principal



#création du mot alléatoire
mot = randomWord()
#cration du mot cripté et du nombre de fois qu'apparait la 1er lettre
motFinal=(afficher(mot))
print (motFinal[0])
#permet au joueur je saisir les lettres
jouer=jouerAffichage(mot,motFinal[0],motFinal[1])
print(winLose(mot,jouer[0],jouer[1],jouer[2],motFinal[1]))


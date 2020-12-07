#@Copyright: Joris CLEMENT
#Header
"""
ce programme permet de jouer au pendu en interface graphique.
Vous avez 8 essais pour découvrir le mot
Auteur: Joris CLEMENT.
date de réalisation: 23/11/2020
"""
"""
TODO -adapter la fonction jouerAffichage a l'interface graphique 
     
     -faire une fonction qui a chaque erreur change l'image

"""

#Importation des bibliothéques
import random

from tkinter import Tk, Label, Button, Entry,PhotoImage,Canvas
#Fonction nécessaires au programme

from TP2_lib import randomWord, afficher, jouerAffichage

#importation du mot
mot=randomWord()

#criptage du mot pour le masqué au joueur
motCripte=afficher(mot)
motFinal=motCripte[0]

#récupération du nombre de fois qu'apparait la 1er lettre
lettre1=motCripte[1]

#création de la fenétre
f=Tk()
f.title("Jeu du pendu")
f.geometry("1200x700+250+200")

#création de l'entry pour saiir une lettre
champ= Entry(f,textvariable = 'entrer votre lettre')
lettre=champ.get()
champ.focus_set()
champ.pack(side="bottom")


#création d'un bouton pour valider la réponse et commencer a jouer
butonProposer= Button(f,text='Proposer',command=jouerAffichage(lettre,mot,motFinal,lettre1))
butonProposer.pack(side="bottom",)

#création d'un canvas pour afficher l'image 
canvas1=Canvas(f, width =400, height =400, bg ='grey')
photo = PhotoImage(file ='image/bonhomme1.gif')
item = canvas1.create_image(200, 150, image =photo)
canvas1.place(relx=0.8,rely=0.5,anchor="e")

f.mainloop()


#@Copyright: Joris CLEMENT
import random
from tkinter import Tk, Label, Button, Entry,PhotoImage,Canvas

# la fonction randomWord permet de retouner un mot d'au moins 5 lettres provenant mesMots.txt.

def randomWord():
    fich = open("mesMots.txt","r")
    a=fich.readlines()
    mot = random.choice(a)
    while (len(mot)-1) < 5:     #permet de prendre les mot de 5 lettres ou plus
        mot = random.choice(a)
    fich.close()
    return mot

# la fonction afficher permet retouner le mot a l'utilisateur sous la forme "e----" par exemple
#si la premiere lettre se retrouve plusieurs fois dans le mot elle sera également afficher.
def afficher(mot):
    mot=mot.lower()
    motFinal=''
    lettre1=0
    for i in range (len(mot)-1): #création du mot maqué
        if mot[i] == mot[0]:
            motFinal += mot[i]
            lettre1+=1              #variable permettant de trouver le nombre de fois que la 1er lettre apparait (utile plus tard pour la consition de victoire)
            
                
        else:
            motFinal += "-"
       
          

    return motFinal,lettre1


# la fonction jouer propose a l'utilisateur de saisir des lettres pour tenter de trouver le mot
#l'utilisateur a le droit a 8 chances
def jouer(mot,motFinal,lettre1):
    LmotFinal=list(motFinal)
    win=0
    essai=0
    while essai != 8 and (len(mot)-1)-lettre1 != win : #condition sur l'arret du jeu, avec condition de victoire/condition de défaite
                                                        #lorque que le joueur à consommé ses 8 chances (en se trompant) et lorsque qu'il a trouvé suffisament de lettre dans le mot pour le découvrir totalement 

        lettre = input("saisir votre lettre : ")
        for i in range (len(mot)-1) :
            if mot[i]==lettre:
                LmotFinal[i] = lettre
                win+=1                              #variable permettant de contabiliser les succés du joueur, utile pour la condition de victoire
        print("".join(LmotFinal))
        
               
        if lettre not in mot:
            essai += 1
            print( "il n'y a pas votre lettre dans le mot, il ne vous reste plus que ",8-essai,"chances")
    return LmotFinal,essai,win

        

    
#cette fonction permet d'afficher au joueur si il gagné ou perdu en lui retournant le mot
def winLose(mot,LmotFinal,essai,win,lettre1):

    
    if win == ((len(mot)-1)-lettre1):
        return "vous avez gagné"
    elif essai == 8: 
        return "vous avez perdu, le mot était "+mot




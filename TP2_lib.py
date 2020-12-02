import random


def randomWord():
    fich = open("mesMots.txt","r")
    mot = random.choice(fich.readlines())
    while (len(mot)-1) < 5:
        mot = random.choice(fich.readlines())
    fich.close()
    return mot


def afficher(mot):
    mot=mot.lower()
    motFinal=''
    for i in range (len(mot)-1):
        if mot[i] == mot[0]:
            motFinal += mot[i]
        else:
            motFinal += "-"
    return motFinal



def jouer(essai,mot,motFinal):
    a=list(motFinal)
    while essai != 8 or '-' not in a:

        lettre = input("saisir votre lettre : ")
        for i in range (len(mot)-1) :
            if mot[i]==lettre:
                a[i] = lettre
#                motFinal="".join(a)
                
                print(a)
               
        if lettre not in mot:
            essai += 1
            print( "il n'y a pas votre lettre dans le mot, il ne vous reste plus que ",8-essai,"chances")
    return mot

        

    





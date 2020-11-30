import random


def randomWord():
    fich = open("mesMots.txt","r")
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
            motFinal += " _ "
    return motFinal


mot= randomWord()
print (mot)
print(afficher(mot))


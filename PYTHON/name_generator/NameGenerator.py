# info (option ecriture lecture fichier) : https://docs.python.org/3/library/functions.html#open

# v0.1 - consonnes + voyelles + nombres
# def nameGeneratorV1():
"""RANDOM PASSWORD ?? -> NAME GENERATOR -> STRING + NUMBER"""
#     #doc string : https://docs.python.org/3.4/library/string.html?highlight=string%20module#string-constants
#     import string
#     import random
#     randomName = ""
#     liste_char = string.ascii_letters + string.digits # letter + alpha numerique
#     for i in range(0, 10):
#         randomName += liste_char[random.randint(0,len(liste_char)-1)]
#     return randomName
# TEST :
# print("Random name -> ", nameGeneratorV1())
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# v0.2 - consonnes + voyelles alternés
# -> nameGeneratorV2():
"""RANDOM NAME GENERATOR -> STRING ONLY -> alterne voyelles/consonnes"""

# TODO : si n, m, l, s, p -> 15% chance de doubler le carractere
#        si p -> 5% chance de faire "ph"
# TODO : ne pas avoir 2 fois le même nom !
#        si nom_creer in FICHIER TXT -> skip and i - 1

def randomName():
    import random

    randomName = ""
    lengthName = random.randint(4, 7) # choisit un nombre au hasard [ 4, 7 ]
    voyelles = ["a", "o", "e", "u" ,"i" , "y"]
    consonnes = [ "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    boiteALettre = [voyelles, consonnes] # ne sert que pour definir si la premiere lettre (lettreUn) est voyelle ou consonne

    for i in range(lengthName-1):
        # Melange
        random.shuffle(boiteALettre)
        random.shuffle(voyelles)
        shuffledVoyelles = voyelles[0]
        random.shuffle(consonnes)
        shuffledConsonnes = consonnes[0]

        if len(randomName) == 0:
            lettreUn = boiteALettre[0][0]
            randomName += lettreUn.upper()
            # continue

        if lettreUn in voyelles:
            if i % 2 == 0:
                lettre = shuffledConsonnes
                randomName += lettre
            else:
                lettre = shuffledVoyelles
                randomName += lettre
        else:
            if i % 2 == 0:
                lettre = shuffledVoyelles
                randomName += lettre
            else:
                lettre = shuffledConsonnes
                randomName += lettre
    return randomName

def verifInputNumber(message):
    """ verif que les input soient : -des entiers -pas des strings -pas vide"""
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Ceci n'est pas un nombre valide ! essayez à nouveau :")
            continue
        else:
            return userInput 

def howMany(fonction):
    """ Multiply le nombre de fois ou une fonction sera print """
    choix = verifInputNumber("Combien de nom voulez-vous ?\n")
    print ("-------- VOICI LA LISTE --------")
    for i in range(choix):
        nom = fonction() # sans la variable, les noms affiché et noms dans fichiers sont differents !
        # ecrire les x noms dans un fichier text

# catch one error
        try:
        # with open("D:/listeNom.txt" , "a") as f: # Maison
            with open("F:/GoogleDrive/_Ordinateur_AFPA/Exercices/Projet_b2A/listeNom.txt" , "a") as f: # Afpa
                f.write(nom + "\n")
                f.close()
        except:
            print ("exept -> error catch'd")
            with open("F:/GoogleDrive/_Ordinateur_AFPA/Exercices/Projet_b2A/listeNom.txt" , "a") as f: # Afpa
                f.write(nom + "\n")
                f.close()
                # ecrire message d'erreur dans un fichier
                # help : https://docs.python.org/fr/2/tutorial/errors.html
            # with open("C:/Users/34011-68-10/Documents/Ordinateur - AFPA/Exercices/Projet b2A/errorlog.txt" , "a") as e: # Afpa
            #     e.write(nom + "\n") # nom qui a bug
            #     e.write("\n" )
            #     e.close()           
        # / nom fichier + message erreur + position de i / choix
        print(nom)
    print ("-------- FIN DE LA LISTE -------\n")

howMany(randomName)




#### Fonction secondaire
"""
Ce docstring est inutile
"""
import math


def ispalindrome(p):
    """
    Une documentation
    """
    #Traitement de la chaine de caractères
    trans_in = "àéêçèôë"
    trans_out = "aeeceoe"
    translation_table = str.maketrans(trans_in, trans_out)

    p = p.lower().replace(" ", "")
    p = ''.join(char for char in p if char.isalnum())
    p = p.translate(translation_table)

    l = len(p)
    for i in range(math.floor(l/2)):
        if p[i] != p[l - (i+1)]:
            return False
    return True

#### Fonction principale


def main():
    """
    Une documentation
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()

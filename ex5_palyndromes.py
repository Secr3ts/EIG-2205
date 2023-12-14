# Vos import ici

def pal(s):
    """
    Teste si s est un palindrome.

    Args:
        s: chaine de caractÃ¨res

    Returns:
        True or False
        
    >>> pal("ressasser")
    True
    >>> pal("Hannah")
    True
    >>> pal("Engage le jeu que je le gagne")
    True
    >>> pal("Esope reste ici et se repose")
    True
    >>> pal("Elu par cette crapule")
    True
    >>> pal("Cette phrase n'est pas un palindrome")
    False
    """
    
    # Ecriture "bas niveau"
    # i = 0
    # j = len(s) - 1
    # while i < j:
    #     while s[i] == ' ': i +=1
    #     while s[j] == ' ': j -=1
    #     if s[i].lower() != s[j].lower():
    #         return False
    #     i += 1
    #     j -= 1
    # return True

    # Ecriture Pythonique (3 lignes max)
    # 1. s1 = la chaine s transformÃ©e en Ã©liminant les espaces et la casse
    # 2. s2 = la chaine s1 Ã©crite de droite Ã  gauche
    # 3. retourner la vÃ©ritÃ© de s == s2

    s1 = s.lower().replace(' ', '')
    s2 = s1[::-1]
    
    
    return s1 == s2


def main():
    # votre code de test ici...
    # Exemple :
    # result = pal('kayak')
    # print(result)
    pass

if __name__ == '__main__':
    main()
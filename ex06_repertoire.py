from genericpath import isdir, isfile
import os

# Exercice 6.1 Contenu d'un rÃ©pertoire

def scand(r):
    """
    SÃ©pare les fichiers et les rÃ©pertoires du rÃ©pertoire passÃ© en argument

    Args:
        r: rÃ©pertoire Ã  analyser

    Returns:
        Liste des noms de fichier sous forme de chaine de caractÃ¨res
        Liste des noms de rÃ©pertoire sous forme de chaine de caractÃ¨res
    >>> f, d = scand('C:\Windows')
    >>> isinstance(f, list) # vrai si f est une liste
    True
    >>> len(f) == 0
    False
    >>> isinstance(d, list) # vrai si d est une liste
    True
    >>> len(d) == 0
    False
    """
    # le contenu des rÃ©pertoires Ã©tant dÃ©pendant de la configuration
    # les doctests sont limitÃ©s

    # crÃ©er la liste du contenu du rÃ©pertoire
    # une list comprehension f pour filtrer les fichiers
        
    f = [x for x in os.listdir(r) if isfile(os.path.join(r, x))]
    # une list comprehension d pour filtrer les rÃ©pertoires
    d = [x for x in os.listdir(r) if isdir(os.path.join(r, x))]
    return f, d
    


def main():
    # votre code de test ici...
    # Exemple
    # f, d = scand('C:\Windows')
    # print(f)
    # print(d)
    f ,d = scand("/Users/gr4ve/Documents")
    print(f)
    print(d)
    
    pass

if __name__ == '__main__':
    main()
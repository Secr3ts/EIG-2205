# vos imports ici

import random


FILENAME = "ex09-mots-data.txt"

def liste_mots(filename):
    """retourne les mots contenus dans filename

    Args:
        filename (str): nom du fichier

    Returns:
        list: la liste des mots

    >>> mots = liste_mots(FILENAME)
    >>> isinstance(mots, list)
    True
    >>> len(mots)
    336531
    >>> mots[1]
    'à'
    >>> mots[328570]
    'vaincre'
    >>> mots[290761]
    'sans'
    >>> mots[233574]
    'péril'
    >>> mots[221712]
    'on'
    >>> mots[324539]
    'triomphe'
    >>> mots[290761]
    'sans'
    >>> mots[166128]
    'gloire'
    """
    l = []
    
    with open(filename, mode='r', encoding='utf8') as file:
        lines = file.readlines();
        l = [s.replace("\n", "") for s in lines]
    return l

def ensemble_mots(filename: str):
    """retourne les mots contenus dans filename

    Args:
        filename (str): nom du fichier

    Returns:
        list: la liste des mots

    >>> mots = ensemble_mots(FILENAME)
    >>> isinstance(mots, set)
    True
    >>> len(mots)
    336531
    >>> "glomérules" in mots
    True
    >>> "glycosudrique" in mots
    False
    """
    mots = {i for i in liste_mots(filename)}
    return mots

def mots_de_n_lettres(mots: set, n: int):
    """retourne le sous ensemble des mots de n lettres

    Args:
        mots (set): ensemble de mots
        n (int): nombre de lettres

    Returns:
        set: sous ensemble des mots de n lettres

    >>> mots = ensemble_mots(FILENAME)
    >>> m15 = mots_de_n_lettres(mots, 15)
    >>> isinstance(m15, set)
    True
    >>> len(m15)
    8730
    >>> list({ len(mots_de_n_lettres(mots,i)) for i in range(15,26)})
    [4418, 2, 4, 2120, 42, 11, 205, 977, 437, 8730, 94]
    >>> sorted(list(mots_de_n_lettres(mots,23)))[0]
    'constitutionnalisassent'
    >>> sorted(list(mots_de_n_lettres(mots,24)))
    ['constitutionnalisassions', 'constitutionnaliseraient', 'hospitalo-universitaires', 'oto-rhino-laryngologiste']
    >>> sorted(list(mots_de_n_lettres(mots,25)))
    ['anticonstitutionnellement', 'oto-rhino-laryngologistes']
    """
    s = {word for word in mots if len(word) == n}
    return s


def mots_avec(mots: set[str], l: str):
    """retourne le sous ensemble des mots incluant la lettre l

    Args:
        mots (set): ensemble de mots
        l (str): lettre à inclure

    Returns:
        set: sous ensemble des mots incluant la lettre l

    >>> mots = ensemble_mots(FILENAME)
    >>> mk = mots_avec(mots, 'k')
    >>> isinstance(mk, set)
    True
    >>> len(mk)
    1621
    >>> sorted(list(mk))[35:74:7]
    ['ankyloseraient', 'ankyloserons', 'ankylostome', 'ankylosée', 'ashkénaze', 'bachi-bouzouks']
    >>> sorted(list(mk))[147:359:38]
    ['black', 'blackboulèrent', 'cheikhs', 'cokéfierais', 'dock', 'dénickeliez']
    >>> sorted(list(mk))[999::122]
    ['képi', 'nickela', 'parkérisiez', 'semi-coke', 'stockais', 'week-end']
    """
    s = set()
    s = {str(word) for word in mots if l in word}
    return s

def main():

    mots = liste_mots(FILENAME)
    
    print(mots[28281])
    
    if "chronophage" not in mots or "procrastinateur" not in mots or "dangerosité" not in mots or "gratifiant" not in mots:
        print("non présent")
    m7: set[str] = mots_de_n_lettres(ensemble_mots(FILENAME), 7)
    
    print(random.sample(list(m7), 7))
    
    print(random.sample(list(mots_avec(ensemble_mots(FILENAME), "k")), 7))
    print(random.sample(list(mots_avec(ensemble_mots(FILENAME), "w")), 7))
    print(random.sample(list(mots_avec(ensemble_mots(FILENAME), "z")), 7))
    print()
    
    mk = mots_avec(ensemble_mots(FILENAME), "k")
    print(len(mots_de_n_lettres(mk, 7)))
    print()
    
    mz = mots_avec(ensemble_mots(FILENAME), "z")
    stwz = {word for word in mz if word.startswith("z")}
    print(random.sample(list(stwz), 7))
    print()
    
    enwz = {word for word in mz if word.endswith("z")}
    print(random.sample(list(enwz), 7))
    print()
    
    hasz = {word for word in mz if word not in stwz and word not in enwz}
    print(random.sample(list(hasz), 7))
    print()
    
    haskz = {word for word in hasz if "k" in word}
    print(random.sample(list(haskz), 7))
    print()

if __name__ == "__main__":
    main()
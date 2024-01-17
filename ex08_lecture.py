import os

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier Ã  lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    >>> data = read_data("data.csv")
    >>> isinstance(data, list)
    True
    >>> isinstance(data[0], list)
    True
    >>> len(data)
    100
    >>> len(data[37])
    10
    >>> data[37]
    [71, 84, 98, 81, 46, 67, 45, 56, 70, 47]
    >>> data[53]
    [61, 37, 55, 59, 96, 94, 86, 98, 81, 64]
    """
    
    with open(filename) as csvFile:
        lines = csvFile.readlines()
        data = []
        for line in lines:
            nline = line.replace("\n", "").split(";")
            nline = list(map(int, nline))
            data.append(nline)
        return data
            

def get_elt_k(data: list[list], k: int):
    """retourne la liste des Ã©lÃ©ments d'indice k de la liste de listes <data>

    Args:
        data (list[list]): liste de listes
        k (int): indice des Ã©lÃ©ments Ã  rÃ©cupÃ©rer

    Returns:
        list: liste des Ã©lÃ©ments d'indice k
    >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> get_elt_k(data, 0)
    [1, 4, 7]
    >>> get_elt_k(data, 1)
    [2, 5, 8]
    >>> get_elt_k(data, 2)
    [3, 6, 9]
    """
    res = []
    for list in data:
        res.append(list[k])
        
    return res

def get_first(data: list):
    return data[0]

def get_last(data: list):
    return data[-1]

def get_max(data: list):
    return max(data)

def get_min(data: list):
    return min(data)


def main():
    data = read_data('data.csv')
    
if __name__ == '__main__':
    main()

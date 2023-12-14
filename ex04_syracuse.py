def syracuse(n: int):
    """
    :param n: an integer.
    Calcule les termes de la suite de Syracuse.
    :return: a tuple with 3 metrics
    """
    u0 = n;
    uk = u0;
    k = 0;
    while uk != 1:
        if uk % 2 == 0:
            uk = uk / 2;
            k += 1;
        else:
            uk = 3 * uk + 1;
            k += 1;
    tv = k;
    
    uk = u0;
    k = 0;
    
    while uk < u0:
        if uk % 2 == 0:
            uk = uk / 2;
            k+=1;
        else:
            uk = 3 * uk + 1;
            k+=1;
    tva = k;
    
    # recherche de maximum
    uk = u0;
    max = uk;
    while uk != 1:
        if uk % 2 == 0:
            uk = uk / 2;
        else:
            uk = 3 * uk + 1;
        if uk > max:
            max = uk;
            
    maxv = max;
    
    return (tv, tva, maxv);
    

def main():
    n1 = 15;
    n2 = 127;
    
    print("Syracuse de ", n1, " : ", syracuse(n1));
    print("Syracuse de ", n2, " : ", syracuse(n2));

if __name__ == '__main__':
    main()
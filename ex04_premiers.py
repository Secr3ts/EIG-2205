def est_premier(n: int):
    """
    :param n: an integer that is or isn't prime.
    
    Return True if n is a prime number, False otherwise.
    """
    i: int = 2;
    for i in range(2, n):
        if n % i == 0:
            return False;
    return True;


def main():
    """
    Print the first 100 prime numbers.
    """
    ctr = 0;
    i = 2;
    while ctr < 100:
        if est_premier(i):
            print(i);
            ctr += 1;
        i += 1;

if __name__ == '__main__':
    main()
    
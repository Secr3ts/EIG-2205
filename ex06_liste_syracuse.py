# imports
import math
import plotly.express as px
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(l, d, f):
    title = "Syracuse" + " (n = " + str(l[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(l)) ]
    t = Scatter(x=x, y=l, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    x = [ i for i in range(len(d)) ]
    t = Scatter(x=x, y=d, mode="lines+markers", marker_color = "red")
    fig.add_trace(t)
    x = [ i for i in range(len(f)) ]
    t = Scatter(x=x, y=f, mode="lines+markers", marker_color = "green")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    >>> l = syracuse_l(129)
    >>> isinstance(l, list)
    True
    >>> len(l)
    122
    >>> l[15:19]
    [188, 94, 47, 142]
    >>> syracuse_l(3)
    [3, 10, 5, 16, 8, 4, 2, 1]
    >>> syracuse_l(4)
    [4, 2, 1]
    >>> syracuse_l(5)
    [5, 16, 8, 4, 2, 1]
    >>> syracuse_l(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> len(syracuse_l(27))
    112
    >>> len(syracuse_l(31))
    107
    >>> len(syracuse_l(41))
    110
    """
    l = [ n ]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)

    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    >>> temps_de_vol(syracuse_l(3))
    8
    >>> temps_de_vol(syracuse_l(4))
    3
    >>> temps_de_vol(syracuse_l(5))
    6
    >>> temps_de_vol(syracuse_l(6))
    9
    """
    n = 1
    for i in l:
        if i != 1:
            n += 1
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    >>> temps_de_vol_en_altitude(syracuse_l(3))
    7
    >>> temps_de_vol_en_altitude(syracuse_l(4))
    2
    >>> temps_de_vol_en_altitude(syracuse_l(5))
    4
    >>> temps_de_vol_en_altitude(syracuse_l(6))
    2
    """
    n = 1
    
    for i in l:
        if i < l[0]:
            break
        else:
            n += 1
    
    return n

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    >>> altitude_maximale(syracuse_l(3))
    16
    >>> altitude_maximale(syracuse_l(4))
    4
    >>> altitude_maximale(syracuse_l(5))
    16
    >>> altitude_maximale(syracuse_l(6))
    16
    """
    n = 0
    
    for i in l:
        if i > n:
            n = i
    
    return n



def main():
    s1 = syracuse_l(15)
    s2 = syracuse_l(127)
    print(s1)
    print(s2)
    
    print(temps_de_vol(s1))
    print(temps_de_vol(s2))

    m = temps_de_vol(syracuse_l(1))

    for n in range(2, 9999):
        l = syracuse_l(n)
        m = max(m, temps_de_vol(l))

    print(m, " bite")
    
    print(temps_de_vol_en_altitude(s1))
    print(temps_de_vol_en_altitude(s2))
    
    #syr_plot(s1)
    #syr_plot(s2)
    
    s3 = [0.0]
    s4 = [] 
    s5 = [0.0]
    
    for i in range(0, 100):
        s3.append(math.cos(i) + math.sqrt(i))
        s4.append(math.sin(i) - math.sqrt(i))   
    
    for i in range(100, 200):
        s3.append(math.sin(i) + math.sqrt(200 - i))
        s4.append(math.cos(i) - math.sqrt(200 - i))
    
    #s4.append(-10.0)
    syr_plot(s3, s4, s5)
    
if __name__ == "__main__":
    main()
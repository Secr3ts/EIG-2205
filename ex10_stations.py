# vos import ici...

from collections import namedtuple
import csv
import re


FILENAME = 'ex08-zip-data-meteo-france-stations.csv'

def build_stations_dict(csvfile):
    """
    retourne un dictionnaire des stations météo du fichier passé en argument

    Args:
        csvfile: un fichier au format csv contenant une liste de stations météo

    Returns:
        dictionnaire de namedtuple des informations relatives aux stations météo
        
    >>> d = build_stations_dict(FILENAME)
    >>> print(d['NICE'])
    Station(ID='07690', Latitude=43.648833, Longitude=7.209, Altitude=2)
    >>> print(d['BELLE ILE-LE TALUT'])
    Station(ID='07207', Latitude=47.294333, Longitude=-3.218333, Altitude=34)
    >>> print(d['CAYENNE-MATOURY'])
    Station(ID='81405', Latitude=4.822333, Longitude=-52.365333, Altitude=4)
    >>> print(d['NICE'].Latitude)
    43.648833
    """
    # votre code ici...
    d = dict()
    keys = ['ID', 'Latitude', 'Longitude', 'Altitude']
    with open(csvfile) as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            Station = namedtuple('Station', keys)
            new_data = Station(*((row[key]) for key in keys))
            
            new_data = Station(row[keys[0]], float(row[keys[1]]), float(row[keys[2]]), int(row[keys[3]]) )
            
            d[row['Nom']] = new_data

    return d

def main():
    d = build_stations_dict(FILENAME)
    print(d['NICE'])
    pass

if __name__ == '__main__':
    main()

import csv
import re

DATA = 'ex08-meteo-data-jan-2014.csv'

def read_meteo_data(filename):
    """Retourne les donnÃ©es mÃ©tÃ©o contenues dans un fichier

    Args:
        filename (str): le nom du fichier

    Returns:
        list: le contenu du fichier

    >>> data = read_meteo_data(DATA)
    >>> isinstance(data, list)
    True
    >>> len(data)
    14299
    >>> data[10][0:7]
    'Alencon'
    >>> data[10][8:10]
    '00'
    >>> data[10][11:13]
    '01'
    >>> data[10][14:16]
    '01'
    >>> data[10][17:21]
    '2014'
    >>> data[10][22:25]
    '5.5'
    >>> data[5338][0:7]
    'Alencon'
    >>> data[5338][8:10]
    '12'
    >>> data[5338][11:13]
    '12'
    >>> data[5338][14:16]
    '01'
    >>> data[5338][17:21]
    '2014'
    >>> data[5338][22:25]
    '7.5'
    """
    with open(filename, "r", -1, "utf8") as file:
        lines = file.readlines()
        data = []
        for i in range(len(lines)):
            if "\n" in lines[i]:
                lines[i] = lines[i].replace("\n", "")
            data.append(lines[i])
        return data

def read_csv_meteo_data(filename):
    """Retourne les donnÃ©es mÃ©tÃ©o contenues dans un fichier csv

    Args:
        filename (str): le nom du fichier

    Returns:
        list: le contenu du fichier sous forme d'une liste de listes

    >>> data = read_csv_meteo_data(DATA)
    >>> isinstance(data, list)
    True
    >>> len(data)
    14299
    >>> isinstance(data[10], list)
    True
    >>> len(data[10])
    6
    >>> data[10]
    ['Alencon', '00', '01', '01', '2014', '5.5']
    >>> data[10][3]
    '01'
    >>> data[10][4]
    '2014'
    >>> data[10][5]
    '5.5'
    >>> data[1234]
    ["Dumont D'Urville", '12', '03', '01', '2014', '4.5']
    >>> data[2345]
    ['Troyes-Barberey', '00', '06', '01', '2014', '8.4']
    >>> data[3456]
    ['Mont-De-Marsan', '09', '08', '01', '2014', '12.3']
    >>> data[4567]
    ['Gillot-Aeroport', '18', '10', '01', '2014', '26.4']
    """
    data = []
    with open(filename, "r", -1, "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            data.append(row)

    return data

def get_meteo_data_by_day(data: list[list[str]], station: str, date):
    """Extrait les donnÃ©es d'une station pour un jour donnÃ©
    

    Args:
        data (list): les donnÃ©es mÃ©tÃ©o
        station (str): le nom de la station mÃ©tÃ©o
        date (str): la date au format jj:mm:aaaa

    Returns:
        list: la liste des tempÃ©ratures

    >>> data = read_csv_meteo_data(DATA)
    >>> d = get_meteo_data_by_day(data, 'Alencon', "12:01:2014")
    >>> isinstance(d, list)
    True
    >>> len(d)
    8
    >>> d
    [0.5, 2.6, 5.5, 6.7, 7.5, 7.9, 6.9, 7.6]
    >>> get_meteo_data_by_day(data, 'Brest-Guipavas', "02:01:2014")
    [8.5, 8.0, 6.5, 9.4, 11.4, 11.1, 10.8, 11.2]
    >>> get_meteo_data_by_day(data, 'brest-guipavas', "02:01:2014")
    [8.5, 8.0, 6.5, 9.4, 11.4, 11.1, 10.8, 11.2]
    >>> get_meteo_data_by_day(data, 'Caen-Carpiquet', "07:01:2014")
    [10.2, 10.2, 10.3, 10.8, 12.5, 12.5, 11.0, 10.1]
    >>> get_meteo_data_by_day(data, 'Lille-Lesquin', "12:01:2014")
    [-0.1, -0.8, -1.3, -0.7, 2.1, 2.9, 3.3, 4.5]
    >>> get_meteo_data_by_day(data, 'Abbeville', "17:01:2014")
    [8.1, 8.2, 7.4, 7.3, 7.0, 7.4, 8.4, 8.2]
    >>> get_meteo_data_by_day(data, 'Brest-Guipavas', "21:01:2014")
    [1.9, 3.3, 5.0, 6.5, 8.6, 9.0, 8.7, 8.7]
    >>> get_meteo_data_by_day(data, 'Orly', "23:01:2014")
    [4.2, 4.6, 4.9, 5.7, 8.2, 6.4, 7.1, 5.1]
    >>> get_meteo_data_by_day(data, 'Strasbourg-Entzheim', "27:01:2014")
    [5.1, 5.5, 5.6, 5.0, 3.5, 5.5, 4.5, 3.7]
    >>> get_meteo_data_by_day(data, 'Bourges', "31:01:2014")
    [0.5, -0.9, -1.4, 0.5, 7.4, 8.8, 6.3, 6.0]
    >>> get_meteo_data_by_day(data, 'Pte De Chassiron', "32:01:2014")
    []
    >>> get_meteo_data_by_day(data, 'Belle Ile-Le Talut', "12:01:2019")
    []
    >>> get_meteo_data_by_day(data, 'Belle Ile-Le Talut', "12:01:2019")
    []
    >>> get_meteo_data_by_day(data, 'London', "12:01:2014")
    []
    """
    temps = []
    date = date.split(":")
    station.capitalize()

    for row in data:
        if row[0] == station and row[2:5] == date:
            temps.append(row[-1])
            
    return temps

def main():
    pass
    data = read_meteo_data(DATA)
    data = read_csv_meteo_data(DATA)

    
    d = get_meteo_data_by_day(data, 'Bourges', "31:01:2014")
    print(d)

if __name__ == "__main__":
    main()
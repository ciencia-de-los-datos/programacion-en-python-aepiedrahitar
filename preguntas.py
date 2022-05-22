"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
import collections

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    col_sum = 0
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            col_sum += int(row[1])
    return col_sum

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    response = []
    col_1 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            col_1.append(row[0]) 
    col_1_elements_type = list(set(col_1))
    col_1_elements_type.sort()
    count_col = collections.Counter(col_1)
    for element in col_1_elements_type:
        element_tuple = (element, count_col[element])
        response.append(element_tuple)


    return response

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    response = []
    csv_list = []
    col_1 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_1.append(row[0]) 
    col_1_elements_type = list(set(col_1))
    col_1_elements_type.sort()
    for element in col_1_elements_type:
        element_sum = 0
        for sub_element in csv_list:
            if element == sub_element[0]:
                element_sum += int(sub_element[1]) 
        response.append((element,element_sum))    
  
    return response

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    response = []
    csv_list = []
    col_3 = []
    month_list = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_3.append(row[2]) 
    for date in col_3:
        month = date[5:-3]
        month_list.append(month)
    month_ordered_list = list(set(month_list))
    month_ordered_list.sort()        
    count_month = collections.Counter(month_list)
    for element in month_ordered_list:
        response.append((element, int(count_month[element])))     
              
    return response



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    response = []
    csv_list = []
    col_1_2 = []
    col_1 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_1_2.append({row[0]:row[1]})
            col_1.append(row[0])
    col_1_elements = list(set(col_1))
    col_1_elements.sort()
    for element in col_1_elements:
        max_min_list = []
        max_value = 0
        min_value = 0
        for sub_element in col_1_2:
            if element in sub_element:
                max_min_list.append(sub_element[element])
        max_value = max(max_min_list)
        min_value = min(max_min_list)
        response.append((element, int(max_value), int(min_value)))
    return response

print(pregunta_05())    


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    response = []
    csv_list = []
    col_5 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_5.append(row[4]) 
    split_col_5 = []
    dict_col_5 = [] 
    key_col_5 = []       
    for element in col_5:
        split_element = []
        split_element = element.split(",")
        for sub_element in split_element:
            split_col_5.append(sub_element)
    for element in split_col_5:
        split_element = element.split(":")
        dict_col_5.append({split_element[0]:int(split_element[1])})  
        key_col_5.append(split_element[0])  
    key_col_5_ordered = list(set(key_col_5))
    key_col_5_ordered.sort()
    for element in key_col_5_ordered:
        max_min_list = []
        max_value = 0
        min_value = 0
        for sub_element in dict_col_5:
            if element in sub_element:
                max_min_list.append(sub_element[element])
        max_value = max(max_min_list)
        min_value = min(max_min_list)
        response.append((element, min_value, max_value))    


    return response

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    response = []
    csv_list = []
    col_1 = []
    col_2 = []
    col_1_2 = []
    col_2_1 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_1.append(row[0])
            col_2.append(int(row[1]))
            col_1_2.append({row[0]:row[1]})
            col_2_1.append({row[1]:row[0]})      
    col_2_ordered = list(set(col_2))
    col_2_ordered.sort()
    for element in col_2_ordered:
        col_1_element_list = []
        for sub_element in col_2_1:
            if str(element) in sub_element:
                col_1_element_list.append(sub_element[str(element)])   
        response.append((int(element),col_1_element_list))       
    return response

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    response = []
    csv_list = []
    col_1 = []
    col_2 = []
    col_1_2 = []
    col_2_1 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_1.append(row[0])
            col_2.append(int(row[1]))
            col_1_2.append({row[0]:row[1]})
            col_2_1.append({row[1]:row[0]})      
    col_2_ordered = list(set(col_2))
    col_2_ordered.sort()
    for element in col_2_ordered:
        col_1_element_list = []
        for sub_element in col_2_1:
            if str(element) in sub_element:
                col_1_element_list.append(sub_element[str(element)])   
        col_1_element_list_ordered=list(set(col_1_element_list))
        col_1_element_list_ordered.sort()
        response.append((int(element),col_1_element_list_ordered))       
    return response

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    response = {}
    csv_list = []
    col_5 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_5.append(row[4]) 
    split_col_5 = []
    dict_col_5 = [] 
    key_col_5 = []       
    for element in col_5:
        split_element = []
        split_element = element.split(",")
        for sub_element in split_element:
            split_col_5.append(sub_element)
    for element in split_col_5:
        split_element = element.split(":")
        dict_col_5.append({split_element[0]:int(split_element[1])})  
        key_col_5.append(split_element[0])
    key_col_5_count = collections.Counter(key_col_5) 
    key_col_5_ordered = list(set(key_col_5))
    key_col_5_ordered.sort()
    for element in key_col_5_ordered:
        response[element] = key_col_5_count[element]
    return response

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    response = []
    csv_list = []
    col_1 = []
    col_4 = []
    col_5 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_1.append(row[0])
            col_4.append(row[3])
            col_5.append(row[4]) 
    split_col_4 = []
    for element in col_4:
        split_element = []
        split_element = element.split(",")
        col_4_count = len(split_element) 
        split_col_4.append(col_4_count)

    split_col_5 = []
    for element in col_5:
        split_element = []
        split_element = element.split(",")
        col_5_count = len(split_element) 
        split_col_5.append(col_5_count) 

    for element_col_1, element_col_4, element_col_5 in zip(col_1, split_col_4, split_col_5):
        response.append((element_col_1,element_col_4,element_col_5))       
    return response

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    response = {}
    pre_response = {}
    csv_list = []
    col_2 = []
    col_4 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_2.append(row[1])
            col_4.append(row[3]) 
    split_col_4 = []
    for element in col_4:
        split_element = element.split(",")
        split_col_4.append(split_element)
    for element_1, element_2 in zip(col_2, split_col_4):
        for sub_element in element_2:
            if sub_element in pre_response:
                pre_response[sub_element] += int(element_1)
            else:
                pre_response[sub_element] = int(element_1)  
    response_sorted = sorted(pre_response) 
    for element in response_sorted:
        response[element] = pre_response[element]
    return response
  
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    pre_response = {}
    response = {}
    csv_list = []
    col_1 = []
    col_5 = []
    with open('data.csv', newline='') as File:  
        reader = csv.reader(File, delimiter='\t')
        for row in reader:
            csv_list.append(row)
            col_1.append(row[0]) 
            col_5.append(row[4])
    split_col_5 = []
    for element in col_5:
        split_element = element.split(",")
        split_col_5.append(split_element)  
    for element_1,element_2 in zip(col_1, split_col_5):
        for sub_element in element_2:
            split_sub_element = sub_element.split(":")
            if element_1 in pre_response:
                pre_response[element_1] += int(split_sub_element[1])
            else:
                 pre_response[element_1] = int(split_sub_element[1])
    response_sorted = sorted(pre_response) 
    for element in response_sorted:
        response[element] = pre_response[element]
    return response                

print(pregunta_12())

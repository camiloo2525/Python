#def get_population():
 # keys = ['Colombia', 'Peru', 'Argentina']
 #values = [500, 250, 350]
 # return keys, values

# variable descripcion
#Descripcion = " Colombia tiene mas numero de habitantes que venezuela "

# def population_by_countrie(data, country): 
  #result = list(filter(lambda item: item['country'] == country, data))
  #return result

def get_population (pais_diccionario):
    poblacion = {
        " 2022 ": int(pais_diccionario[" 2022 poblacion "]),
        " 2020 ": int(pais_diccionario[" 2020 poblacion "]),
        " 2015 ": int(pais_diccionario[" 2015 poblacion "]),
        " 2010 ": int(pais_diccionario[" 2010 poblacion "]),
        " 2000 ": int(pais_diccionario[" 2000 poblacion "]),
        " 1990 ": int(pais_diccionario[" 1990 poblacion "]),
        " 1980 ": int(pais_diccionario[" 1980 poblacion "]),
        " 1970 ": int(pais_diccionario[" 1970 poblacion "])
    }
    labels =  poblacion.keys
    values = poblacion.values(),
    return labels , values

def population_by_countrie(data, country): 
  result = list(filter(lambda item: item['country'] == country, data))
  return result
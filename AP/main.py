import utils
import leer_csv
import graficos

def ejecutar():
  data = leer_csv.leer_csv("./AP/data.csv")

  country = input(" que pais es ")

  result = utils.population_by_countrie(data, country)

  if len(result)>0:
    country = result[0]

  labels, values = utils.get_population(country)

  graficos.generador(labels,values)
  if __name__ == "__main__":
   ejecutar()
  
  #print(keys, values)

  # variable descripcion
  #print(utils.Descripcion)
"""
  data = [
  {
  'country': 'Colombia',
  'Population': 500
  },
  {
  'country': 'Peru',
  'Population': 250
  },
  {
  'country': 'Argentina',
  'Population': 350
  }
  ]

  country = input('Digite el país: ')
  result = utils.population_by_countrie(data, country)
  print(result)
"""

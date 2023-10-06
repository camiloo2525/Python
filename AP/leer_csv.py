import csv # Importa el módulo csv de la biblioteca estándar de Python

def leer_csv (path):
# Abre el archivo CSV en el modo de lectura ("r") y lo asocia a la variable csvdata
    with open(path , "r") as csvdata:

        # Crea un objeto lector de CSV utilizando csv.reader y configura el delimitador como ";"
        reader = csv.reader(csvdata , delimiter =";")
        header = next(reader)
        data = []


          
        for fila in reader:
            iterable =zip(header,fila)
            
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

           
              # Esta condición verifica si el script se está ejecutando directamente (no importado como módulo)
if __name__ == "__main__":
 
 # Si es así, llama a la función leer_csv con la ruta al archivo CSV "./AP/data.csv"
 data = leer_csv("./AP/data.csv")
 print(data[0])


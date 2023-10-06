import matplotlib.pyplot as plt

def generador(labels, valores):
    
    figura, coordenadas = plt.subplots()
    coordenadas.bar(labels,valores)
    plt.show()

def grafica_torta(labels , valores):
   figura, coordenadas = plt.subplots()
   coordenadas.pie (valores, labels=labels)
   coordenadas.axis("on")
   plt.show()
   # ejecutar modulo como un script
if __name__ == "__main__":
 labels = ["a","b","c"]
 valores = [100,300,500]
 # generador(labels,valores)
 grafica_torta(labels,valores)



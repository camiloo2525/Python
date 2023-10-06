# "r+" permiso de escritura Y LECTURA
# "w+" para no duplicar contenido en txt tambien escritura y lectura
# escribir en un txt

with open ("./text.txt" , "w+") as texto:
  for linea in texto:
    print(linea)
  texto.write (" Nuevas escrituras \n ")
  texto.write (" otra linea \n ")
  texto.write (" otra linea mas \n ")
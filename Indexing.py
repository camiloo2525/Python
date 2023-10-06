#Indexing Indicador de posiciones como arreglos

text = "Ella sabe Python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

#Saber el ultimo caracter del texto
size = len(text)
print("Size=" ,size)
print(text[size-1])
print(text[-1])

# slicing arroja desde que posicion quiero hasta la otra posicion

print(text[0:5])
print(text[10:16])
print(text[0:10])
print(text[:10])
print(text[5:-1])
print(text[5:])
print(text[:])

#Saltos se come letras
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])


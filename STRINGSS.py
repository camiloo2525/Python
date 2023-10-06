text = "Ella sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
    print("Elegiste bien")
else:
    print("Tambien elegiste bien")

# Tamaño de un String contador de letras
size = len("Amor")
print(size)

size = len(text)
print(size)

# Pasa el texto a mayuscula
print(text) 
print(text.upper())

# pasa el texto a minuscula
print(text)
print(text.lower())

# Numero de apariciones de una letra
print(text.count("a"))

# pasa letra de mayuscula a minuscula y de minuscula a mayuscula
print(text.swapcase())

# Verifica si el texto empieza con la palabra que le demos
print(text.startswith("Ella"))

# Verifica si el texto termina con la palabra que le demos
print(text.endswith("Rust"))

# Remplaza una palabra del texto
print(text.replace("Python","Go"))

# Coloca el primer caracter en mayuscula
text2 = "este es un titulo"
print(text2)
print(text2.capitalize())

# Coloca el primer caracter de cada palabra en mayuscula
print(text2.title())

# Nos dice si el texto es un digito o numero
print(text2.isdigit())


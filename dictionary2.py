import random
paises = ["col","vzl","pan","cl"]

poblacion = { pais: random.randint(1,100) for pais in paises}
print(poblacion)

resultado = {pais:poblacio for (pais,poblacio) in poblacion.items()if poblacio>20}
print(resultado)

texto = "Hola soy camilo"
unico = {c: c.upper()for c in texto if c in "aeiou" }
print(unico)

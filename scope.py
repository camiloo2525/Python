"""
Dentro de una función puede haber variables, las cuales se llaman variables locales. Estas variables locales,
se identifican porque están escritas dentro de la definición de la función; y únicamente funcionan mientras que la función
sea llamada o utilizada. Si vas a llamar a una variable local por fuera de la función, no servirá.
Y existen variables globales, que son las que están escritas fuera de una función. 
Estas variables si funcionan al ser llamadas sin la función, porque no están determinadas dentro de la función.
"""

precio = 100 # alcance global 

def incrementar ():
    print(precio)

print(" el precio es: " ,precio)

precio2 = 200 

def incrementar2 ():
    precio2 =200
    result = precio2 + 10
    print(result)
    return result
precio2 = incrementar2()
print(precio2)

externa = "externa"

def funcion (parametro):
    interna = "interna"
    print("adentro",externa,parametro,interna)
funcion("parametro")

"""
Para resolver este desafío, tu reto completar la función message_creator para que retorne un mensaje 
distinto dependiendo del artículo de tecnología que reciba como entrada.
La función message_creator recibirá como entrada un string que indica el artículo de tecnología. Luego, deberás evaluar
el valor de este string y retornar un mensaje distinto dependiendo del valor que reciba.
La implementacion debe responder al siguiente comportamiento:
Si recibes una computadora, debes retornar el mensaje: "Con mi computadora puedo programar usando Python".
Si recibes un celular, debes retornar el mensaje: "En mi celular puedo aprender usando la app de Platzi".
Si recibes un cable, debes retornar el mensaje: "¡Hay un cable en mi bota!".
Y si no recibes ninguno de estos valores, debes retornar el mensaje: "Artículo no encontrado"
"""
def message_creator(text):
   if text == 'computadora':
      return 'Con mi computadora puedo programar usando Python'
   elif text == 'celular':
      return 'En mi celular puedo aprender usando la app de Platzi'
   elif text == 'cable':
      return '¡Hay un cable en mi bota!'
   else:
      return 'Artículo no encontrado'
text = 'computadora'
response = message_creator(text)
print(response)
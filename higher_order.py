def increment (x):
    return x+1
increment_v2 = lambda x: x+1


def high_order_function (x, func):
    return x + func(x)

high_order_function_v2 = lambda x, func : x + func (x)

result = high_order_function(2,increment)
print(result)

result = high_order_function_v2(2,increment_v2)
print(result) 

result = high_order_function_v2(2, lambda x: x + 2)
print(result)

result = high_order_function_v2 (2,lambda x: x * 5)
print(result)

# funciones con orden superior

# upper convierte de minuscula a mayuscula
# lower convierte de mayuscula a minuscula

def gritar(text):
	return text.upper()
	
def silencio(text):
	return text.lower()
	
def saludo(func):
	# almacenar la función en una variable
	conversacion = func("Hi, I am created by a function \
	passed as an argument.")
	print(conversacion)
	
saludo(gritar)
saludo(silencio)

# otro ejemplo

def suma (x,y):
	return x+y

def resta (a,b):
	return a-b

def resultado(func):
	operacion = func(7,5)
	print(operacion)

resultado(suma)
resultado(resta) 
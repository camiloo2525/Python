x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print (x==y)

# para convertir y en string
y_str = format(y, ".2g")
print("str =>" , y_str)
print (y_str == str(x))

# forma matematica
print("*" * 10)
print(y,x)
tolerancia = 0.00001
print(abs(x - y)<tolerancia)



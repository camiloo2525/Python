
numeros = []
for elementos in range(1,11):
    numeros.append(elementos)
    print(elementos * 2)

numeros_V2 = [elementos for elementos in range(1,11)]
print(numeros_V2)

numeros2 = []
for i in range(1,11):
  if i % 2 == 0:
    numeros2.append(i*2)
    print(numeros2)

numeros_v = [i*2 for i in range (1,11) if i%2 ==0]
print(numeros_v)

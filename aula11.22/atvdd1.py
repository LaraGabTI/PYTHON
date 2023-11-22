pares = 0
impar = 0
for i in range(1, 11):
    n = int(input(f'digite {i} numero: '))
    divisao = i%2
    if(divisao % 2 == 0):
        pares += 1
    else:
        impar += 1

print("Quantidade de numeros pares", pares)
print("Quantidade de numeros impares", pares)
        
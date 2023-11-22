maior = 0
lista = []

for i in range(4):
    num = int(input("Infome o numero "))
    lista.append(num)
    if num > maior:
        maior = num
print(lista) 
print("esse é o maior numero", maior) 


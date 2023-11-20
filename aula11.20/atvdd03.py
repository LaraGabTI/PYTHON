cont = 0
maior = 0
lista = []

while cont <= 4:
    num = int(input("Infome o numero "))
    lista.append(num)
    if num > maior:
        maior = num
    
    cont += 1
print(lista) 
print("esse é o maior numero", maior) 


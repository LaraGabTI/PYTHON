maior = 0
menor = None

while True:
    
    s = input("digite s pra sair")
    if(s == "s" or s == "S"):
        print("volte sempre")
        break
    
    n = int(input("digite um numero"))
    
    if (n > maior):
        maior = n
    
    if (menor == None or n < menor):
        menor = n 
    
print(f'Maior numero:  {maior} Menor numero: { menor}')
print(f'A soma dos valores eh: {maior + menor}')

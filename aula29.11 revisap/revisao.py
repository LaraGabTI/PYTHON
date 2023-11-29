#o que é variavel
#quais são iteraveis: strings, listas e sets
#fatiamento

lista = ['a', 'b', 'c', 'd', 'e']

tamanho = len(lista)
print(tamanho)

print(lista)
i = 0
for i in range(tamanho+1):
    print(lista[0:tamanho])
    tamanho -= 1

#print(lista)   
lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

#concatena listas #sinal de mais faz polimorfismo
lista_c = lista_a + lista_b
print (lista_c)

#lista fica como extensão da lista a 
lista_a.extend(lista_b)
print(lista_a)

lista_d = lista_a
print(lista_d)


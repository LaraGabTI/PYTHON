#for é uma estrutura de repetição
# "for" deve ser utilizado em casos que voce sabe a quantidade de repetições
#na maioria das vezes utlizar o metodo range() para montar sa chamada do "for"
#range(i, f, s) - i = inicio, f = fim, s = step(salve) // trabalha com iteraveis
#n precisa passar tpdps, se passar apenas 1 será o valor FIM
#range(5), range(1, 5)

#trabalha com dois metodos, por tras, iter() transforma em obj iteravel e next() e caminha
nome = 'Paulo'
texto = iter(nome)
print(next(texto))

# i - variavel de controle
for i in nome:
    print(i)

for i in range(5):
    print(i)

x = range(1, 5)
for i in x:
   print(i)

#enumarate() é um iterador de indices e valores TUPLA
lista_nomes = ['João', 'Pedro', 'Mateus', 'Judas']
lista_enumerate = enumerate(lista_nomes) #ele é um iteravel, 
print(lista_nomes)
print(list(lista_enumerate)) # p usar tem que usar o metodo list

for item in lista_enumerate:
    print(item)

#primeiro indice, depois o valor #percorre o outro lado
for indice_lista, item_lista in enumerate(lista_nomes):
    print(item_lista, indice_lista)
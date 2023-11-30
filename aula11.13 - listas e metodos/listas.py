#uma lista é representada pelos []
#len - metodo que retorna a quantidade de itens de uma liata
#append - metodo que add item no final da lista
#del - remove itens especificos da lista 
#remove - remove itens pelo o nome
#pop - remove o ultimo objeto da lista, e retorna o removido
#insert - adicionar um objeto no inicio da lista

lista = []
print("lista:", lista, "vazia", type(lista))
print(len(lista)) #retorna a qntt de itens

lista = ['front']
print("lista:", lista, type(lista))
print(len(lista))

#adiciona na lista / atualiza a lista
lista.append('back')
print(lista)
print(len(lista)) 

lista = ['back', 'tarde', 21, True, 8.8]
print(f' a quantidade de alunos na turma eh:{lista[2]}')
lista[2] = 22
print(lista)

#Lista dentro de listra = matriz
lista[1] = ['Lara','Paula', 'Alice']
print(lista)
print(lista[1])
print (lista[1] [1]) 

del lista[-2]
print(lista)

lista.remove('back')
print(lista)

lista.pop ()
print(lista)

valor_do_pop = lista.pop()
print(valor_do_pop)

lista.insert (0, 'back')
print(lista)

lista.insert (3, 'back')
print(lista)
# Set - Conjuntos
#parcialmente imutavel
#parametro chaves, fatia o interavel(numero)
#retorna o conjunto, economiza espaço, n repetindo os caracteres
#apenas para string, só aceita um argumento
#chamando o metodo
#não tem indice

set1 = set('Lara')
set2 = {'Lara', 'Gab'}
print(set2)

#retira os repetidos
lista = [1, 2, 3, 4, 5, 5]
set3 = set(lista)
print(set3)
print(5 in set3)
print(10 in set3)
print(5 not in set3)

for i in set3:
    print(i)

#adiciona o objeto
set3.add('Paulo')
set3.add(1)

#quebra o interavel
set3.update('Paulo')
print(set3)

#deleta o objeto ou o interavel
set3.discard('P')
print(set3)

#limpa todo o set
set3.clear()
print(set3)

set4 = {1, 2, 3, 4}
set5 = {3, 4, 5, 6}

#união
set6 = set4 | set5
print(set6)

#interseção
set6 = set4 & set5
print(set6)

#diferença que ta no primeiro que não ta no segundo
set6 = set4 - set5
print(set6)

#diferença que ta no segundo que não ta no  primeiro
set6 = set5 - set4
print(set6)
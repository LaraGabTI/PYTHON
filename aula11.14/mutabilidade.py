#alguns cuidados com dados mutaveis 
#mutaveis pode ser alterado na memoria do dispositivo
#imutaveis dados que só podem ser copiados na memoria do dispositivo

#string mutaveis, e o conteudo é imutavel, endereço de memoria continua o mesmo
#só que caso eu queira outro, faço outro endereço de memoria

#lista totalmente multavel, e tem o mesmo valor de memoria, 
#lista ela não cria um novo endereço de memoria, só aponta
#lista imutavel, conteudo mutavel

#listaa.copy altera o endereço de memoria

nome = 'Lara'

lista_a = ['lara', 'jose']
lista_b = lista_a
lista_b[1] = 'gabi'
lista_c = lista_a.copy()
lista_c[0] = 'lala'
lista_a[1] = 'baba'
print(lista_a)
print(lista_b)
print(lista_c)


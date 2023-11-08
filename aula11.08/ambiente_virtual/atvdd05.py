#fatiamento de strings
#obs: toda string por padrão é uma listra que não saiu do armario
#ordem de tratamento 
#0123456... #-65321

nome = "Lara"
print(nome[2])
print(nome[-3])

lista_nome = ("L", "a", "r", "a")
print(lista_nome[2])
print(lista_nome[-3])

#estrutura de fatiamento
#[i:f:p] = i - inicio, f - fim, p - parse

nome = "Lara Gabryella"
print(nome[5:8]) #coloca um a mais
print(nome[-4:]) #no negativo pega daqui p la
print(nome[0::2]) #letras que tão no indice par
print(nome[1::2]) #letras que tão no indice impar
print(nome[0::3]) #letras que são multiplos de 3
#count - função é contar quantas x um caractere aparece na str, 
#só conta minusculo, transforma em lower primeiro
#não conta acentos também
frase = "pra ver A banda passar, cantando historias de amor".lower()
print(frase.count('a'))
letra ='a'
print(f'A letra "{letra}" aparece {frase.count(letra)}x na frase: "{frase}"')

#upper - letras maiusculas
#saida = input('Digite "S" para sair').upper()
#saida.upper()
#lower - letras minuscula
#saida = input('Digite "S" para sair').lower()

#find - busca por uma expressão dentro da frase, aparece o indice
print(frase.find('uau'))

achei = frase.find('uau')
if(achei >= 0):
    print(f"expressao encontrada no indice{achei}")
else:
    print("Expressão n foi encontrada na frase")

#replace - utlizado p realizar alterações dentros de str
nova_frase = frase.replace ('historias', 'estorias')
print(frase)
print(nova_frase)
nova_frase2 = frase.replace (' ', '')
print(nova_frase2)

#capitalize - primeira letra das palavras em maiuscula
print(frase.capitalize())

#split - transforma str em lista
print(frase.split())

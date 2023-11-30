#faça uma função que retorne o reverso de um numero interiro informado.
# Por exemplo: 127 -> 721

def numero_reverso(valor):
    numero = str(valor)
    numero_rev = numero[::-1]
    return int(numero_rev)

def numero_rev (numero):
    reverso = 0
    while numero > 0:
        #pega o ultimo valor do numero
        ultimo_valor = numero%10 
       
        #
        reverso = (reverso * 10) + ultimo_valor
       
        #faz divisao e retorna o numero inteiro
        numero = numero // 10

        return reverso
    
numero = int(input('informe um numero: '))
print(numero_reverso(numero))


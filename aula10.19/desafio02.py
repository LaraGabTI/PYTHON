#Receba a altura(h) de uma pessoa, crie um código que calcule seu peso ideal, utilizando as fórmulas abaixo:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo = int(input('Se voce for homem digite 1 e se for mulher digite 2'))

if (sexo == 1):
    h = float (input('Qual é a sua altura'))
    print ("Seu peso ideal eh", (72.7 * h) - 58)
elif (sexo == 2):
    h = float (input('Qual é a sua altura'))
    print ("Seu peso ideal eh", (62.1 * h) - 44.7)
else:
    print ("Infelizmente, não temos essa opção ")
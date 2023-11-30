#funções são blocos de codigos qe são executados somente quando são chamados
#parametros: def
#as funções devem ter prioridades no codigo

def media (nota1, nota2, nota3): #porta de entrada da função ()
    media = (nota1 + nota2 + nota3) / 3
    return media 

nota1 = int(input("Digite a primeira nota"))
nota2 = int(input("Digite a segunda nota"))
nota3 = int(input("Digite a terceira nota"))

print(media(nota1, nota2, nota3))

def calc_horas_extras(qtdd_h, valor_h):
    horas = float(qtdd_h)
    taxa = float(valor_h)

    if horas >= 40:
        valor_receber = (horas - 40) * taxa

        return valor_receber

qtdd_h = float(input("Quantas horas trabalhas?"))
valor = float(input("Valor da hora trabalha?"))

print(calc_horas_extras(qtdd_h, valor))

def cactere(valor1):
    valor = (int(valor1))

    if(valor1 > 0):
        return 'P'
    else:
        return 'N'

valor1 = float(input("Digite o valor"))

print(cactere(valor1))
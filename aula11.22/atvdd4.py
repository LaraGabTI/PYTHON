aumento_anual = 0.3
inicial = 80000
contador = 0
valor_final = inicial

while True:
    aumento = valor_final * aumento_anual
    valor_final += aumento
    contador += 1

    if valor_final >= 120000:
        print(f'Leva {contador} anos para atingir o valor')
        break
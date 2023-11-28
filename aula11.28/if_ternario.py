#condicao ternaria acontece em formato de linha

salario = float(input("Informe o valor do seu salario: "))

if salario >= 2500.00:
    print("IR sera cobrado")

variavel_controle = 'IR será cobrado' if salario >= 2500.00 else 'IR não sera cobrado'
print(variavel_controle)

vr_controle = 'ok 1' if True else 'ok 2' if False else 'fim'

if True: 
    print ("ok 1")
elif False:
    print("Ok 2")
else:
    print('Fim')
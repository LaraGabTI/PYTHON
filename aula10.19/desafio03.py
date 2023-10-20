#Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de 
#reajuste e calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).

salario_atual = float(input('Digite qual é o seu salario atual'))
porcentagem_de_reajuste = float(input('Em quantos porcento seu salario será reajustado?'))
                          
salario_reajustado =  (salario_atual * (100 + porcentagem_de_reajuste) / 100)
print ('Seu salario reajustado será', salario_reajustado)
soma = 0
for i in range(3):
    idade = int(input("diga sua idade"))
    soma += idade 
    
media = soma/3
if media > 0 and media < 25:
    print("turma jovem")
elif media > 26 and media < 60:
    print("turma adulta")
else:
    print("turma idosa")
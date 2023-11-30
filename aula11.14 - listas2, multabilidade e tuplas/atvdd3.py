print ("Digite as notas do primeiro aluno")
n1_aluno1 = float(input('Digite a primeira nota'))
n2_aluno1 = float(input('Digite a segundo nota'))
n3_aluno1 = float(input('Digite a terceira nota'))

print ("Digite as notas do segundo aluno")
n1_aluno2 = float(input('Digite a primeira nota'))
n2_aluno2 = float(input('Digite a segundo nota'))
n3_aluno2 = float(input('Digite a terceira nota'))

print ("Digite as notas do terceiro aluno")
n1_aluno3 = float(input('Digite a primeira nota'))
n2_aluno3 = float(input('Digite a segundo nota'))
n3_aluno3 = float(input('Digite a terceira nota'))

print ("Digite as notas do quarta aluno")
n1_aluno4 = float(input('Digite a primeira nota'))
n2_aluno4 = float(input('Digite a segundo nota'))
n3_aluno4 = float(input('Digite a terceira nota'))

media1 = (n1_aluno1 + n2_aluno1 + n3_aluno1) / 3
media2 = (n1_aluno2 + n2_aluno2 + n3_aluno2) / 3
media3 = (n1_aluno3 + n2_aluno3 + n3_aluno3) / 3
media4 = (n1_aluno4 + n2_aluno4 + n3_aluno4) / 3

medias_dos_alinos = [media1, media2, media3, media4]
print ("media dos quatro alunos", medias_dos_alinos)
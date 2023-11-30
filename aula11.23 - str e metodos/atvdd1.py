str = input("Digite uma string: ")
print(str)
print(len(str))
tam = len(str)

#imprime só as consoantes
for i in range(tam):
    #print(str[i])
    if(str[i] != 'a' and str[i] != 'e' and str[i] != 'i' and str[i] != 'o' and str[i] != 'u'):
        print(str[i])

#imprime só as consoantes
nova_str= str.replace ('a', '')
nova_str= str.replace ('e', '')
nova_str= str.replace ('i', '')
nova_str= str.replace ('o', '')
nova_str= str.replace ('u', '')
print(str)

#quantas vogais tem o nome
vogais = 0
vogais = str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u')
print(f'Str tem {vogais} vogais')

#compara duas strings
str2 = input("Digite outra string: ")
if(str == str2):
    print(f'{str} eh igual a {str2}')
else:
    print("Strings são diferentes")


#imprimir str de tras p frente
print(str[::-1])





    

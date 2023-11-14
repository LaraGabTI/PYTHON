letra1 = input('Digite a primeira letra')
letra2 = input('Digite a segunda letra')
letra3 = input('Digite a terceira letra')
letra4 = input('Digite a quarta letra')
letra5 = input('Digite a quinta letra')

lista_consoante = []

if(letra1 != 'a' and letra1 != 'e' and letra1 != 'i' and letra1 != 'o' and letra1 != 'u'):
    print("É uma consoante")
    lista_consoante.append (letra1)

if(letra2 != 'a' and letra2 != 'e' and letra2 != 'i' and letra2 != 'o' and letra2 != 'u'):
    print("É uma consoante")
    lista_consoante.append (letra2)

if(letra3 != 'a' and letra3 != 'e' and letra3 != 'i' and letra3 != 'o' and letra3 != 'u'):
    print("É uma consoante")
    lista_consoante.append(letra3)

if(letra4 != 'a' and letra4 != 'e' and letra4 != 'i' and letra4 != 'o' and letra4 != 'u'):
    print("É uma consoante")
    lista_consoante.append(letra4)

if(letra5 != 'a' and letra5 != 'e' and letra5 != 'i' and letra5 != 'o' and letra5 != 'u'):
    print("É uma consoante")
    lista_consoante.append(letra5)

print(lista_consoante)
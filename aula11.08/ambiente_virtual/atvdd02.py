entrada = input ("[E] para entrar e [S] para passar: ")
senha_usuario = input("Digite a senha")
senha = "1234567"

if(entrada == 'E' or entrada == 'e'):
    if(senha == senha_usuario):
        print("Bem vindo ao sistema!")
    else:
        print("Senha incorreta")
elif(entrada == 'S' or entrada == 's'):
    print("Voce escolheu passar")
else:
    print("voce não selecionou pra entrar")


   
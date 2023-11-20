tentativas = 0

while tentativas <= 3:
    nome = input("Qual é seu nome? ")
    senha = input("Digite sua senha")
   
    if senha == nome:
        print("sua senha deve ser diferente do seu nome, voce ja tentou", tentativas + 1, "vezes")
        if tentativas == 3:
            print("Suas tentativas acabaram, tente amanhã")
            break
    else:
        print("Logado com sucesso")
        break
     
    tentativas += 1

            




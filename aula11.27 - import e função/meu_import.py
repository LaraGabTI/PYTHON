preco = float(input("Informe o preço do produto"))

desconto1 = 0.2
desconto2 = 0.5
desconto3 = 0.8

valor = preco * desconto2
print(valor)

if preco < 100: 
    valor = preco * desconto1
elif preco >= 100 and preco <= 500:
    valor = preco * desconto2
elif preco > 500:
    valor = preco * desconto3
else:
    print(f'O preco {preco} não se aplica a esse valor')
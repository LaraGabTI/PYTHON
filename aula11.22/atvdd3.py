primo = 0
i = 1
cont = 0

n = int(input("digite um numero"))
for i in range(1, n+1):
    if (n % i == 0):
        cont += 1

if cont==2:
    print(n, "é primo")
else:
    print(n, "não é primo")

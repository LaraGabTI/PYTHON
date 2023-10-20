#Crie um código que peça a temperatura em graus Fahrenheit, transforme e imprima a temperatura em graus Celsius.
#Formula: C = 5 * ((F-32) / 9)

fahrenheit = float(input('Digite a temperatura em fahrenheit'))
celsius = float(5 * ((fahrenheit - 32) / 9))

print (f'Temperatura em fahrenheit {fahrenheit} transformada em celsius eh {celsius}')
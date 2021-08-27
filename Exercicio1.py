numero = float(input('Digite um peso: '))

maior = numero
menor = numero
cont = 1

while (cont != 8):
    num = float(input("Digite outro peso: "))
    if (num > maior):
        maior = num
    if (num < menor):
        menor = num
    cont += 1

print("O menor peso é: ", menor)
print("O maior peso é: ", maior)
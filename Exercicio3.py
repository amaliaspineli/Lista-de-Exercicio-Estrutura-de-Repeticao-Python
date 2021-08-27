total = 0
soma = 0

idade = int(input('Digite a idade: '))

if (idade < 0):
    exit()

menor = idade
maior = idade


while (idade > 0):
    if (idade < menor):
        menor = idade
    if (idade > maior):
        maior = idade
    soma += idade
    total += 1
    idade = int(input('Digite a idade: '))

media = soma / total

print("A menor idade é: ", menor)
print("A maior idade é: ", maior)
print("A idade média é: ", media)
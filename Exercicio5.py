cont = 1

energia = float(input('Digite a quantidade de kWh: '))
custo = energia * 0.3
print("Custo total do consumidor ", cont, "é: ", custo)

menor = energia
soma = energia
indice = 1


while (cont != 6):
    cont += 1
    energia = float(input('Digite a quantidade de kWh: '))
    custo = energia * 0.3
    print("Custo total do consumidor", cont, "é: ", custo)
    if (energia < menor):
        menor = energia
        indice = cont
    soma += energia

media = soma/cont

print("A média de consumo de todos é de:", media, "kWh")
print("O consumidor", indice, "teve o menor consumo de:", menor, "kWh")
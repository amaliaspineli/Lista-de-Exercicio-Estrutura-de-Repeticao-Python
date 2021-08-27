cont = 1
soma = 0
conta = int(input('Digite o numero da conta: '))
saldo = float(input('Digite o saldo: '))
if (saldo >= 0):
    print("A conta de numero", conta, "com o saldo de $", saldo, "está POSITIVO")
else:
    print("A conta de numero", conta, "com o saldo de $", saldo, "está NEGATIVO")
    soma += 1

while (cont != 5):
    cont += 1
    conta = int(input('Digite o numero da conta: '))
    saldo = float(input('Digite o saldo: '))
    if (saldo >= 0):
        print("A conta de numero", conta, "com o saldo de $", saldo, "está POSITIVO")
    else:
        print("A conta de numero", conta, "com o saldo de $", saldo, "está NEGATIVO")
        soma += 1

percentual = soma*100/5

print("O percentual de pessoas com saldo negativo é de: ", percentual, "%")
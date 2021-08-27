nota = float(input('Digite uma média final: '))

aprovados = 0
reprovados = 0
maior = nota
menor = nota
if (nota >= 6):
    aprovados += 1
else:
    reprovados += 1
soma = nota
cont = 1

while (cont != 7):
    nota = float(input('Digite outra média final: '))
    if (nota < menor):
        menor = nota
    if (nota > maior):
        maior = nota
    if (nota >= 6):
        aprovados += 1
    else:
        reprovados += 1
    soma += nota
    cont += 1

media = soma/cont

print("A menor média é: ", menor)
print("A maior média é: ", maior)
print("A média da turma é: ", media)
print("Quantidade de alunos aprovados: ", aprovados)
print("Quantidade de alunos reprovados: ", reprovados)
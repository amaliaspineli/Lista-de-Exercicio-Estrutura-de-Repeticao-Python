import math

numero = int(input("Digite o numero que quer realizar a fatorial: "))
count = numero
fatorial = math.factorial(numero)

if (numero < 1):
    exit()

print(numero, end="! = ")
for i in range(numero - 1):
    print(count, end=" X ")
    count -= 1
print("1 =",fatorial)
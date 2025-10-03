import os
os.system("cls")

lista_numeros = []

print("Solicitando números")
for i in range(5):  
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero < 0:
        lista_numeros.append(0)
    else:
        lista_numeros.append(numero)

print(f"Os valores armazenados foram: {lista_numeros}")
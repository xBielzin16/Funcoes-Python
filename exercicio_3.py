import os
os.system("cls")

# Função com passagem de parâmetros.
# Criando uma função.
def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} X {i} = {numero * i}")

print("Solicitando dados.")
numero = int(input("Digite um número: "))

# Chamando a função.
print("\nExibindo resultados")
tabuada(numero)
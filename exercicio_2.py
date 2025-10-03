import os
os.system("cls")

# Função com passagem de parâmetros.
# Criando uma função.
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

print("Solicitando dados.")
numero = int(input("Digite um número: "))


# Chamando a função.
par_ou_impar(numero)
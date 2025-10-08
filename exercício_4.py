import os
import time

def limpa_tela():
    time.sleep(3)
    os.system("cls")

def somar (n1, n2):
    return n1 + n2

def subtrair (n1, n2):
    return n1 - n2

def multiplicar (n1, n2):
    return n1 * n2    
    
def dividir (n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: divisão por zero"
            

def mostrar_resultado (resultado):
    print(f"\nResultado: {resultado}")

limpa_tela()

print("Escolha a operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção desejada (1/2/3/4): ")

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

if opcao == "1":
    resultado = somar(primeiro_numero, segundo_numero)
elif opcao == "2":
    resultado = subtrair(primeiro_numero, segundo_numero)
elif opcao == "3":
    resultado = multiplicar(primeiro_numero, segundo_numero)
elif opcao == "4":
    resultado = dividir(primeiro_numero, segundo_numero)
else:
    resultado = "Opção inválida!"

mostrar_resultado(resultado)



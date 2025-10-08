import os
os.system("cls")

def metros(metros):
    centimetros = metros * 100
    return centimetros

valor_metros = float(input("Digite um valor em metros: "))
resultado = metros(valor_metros)

print(f"{valor_metros} metros equivalem a {resultado} centímetros.")
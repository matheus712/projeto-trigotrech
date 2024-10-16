import math

def pitagoras(a, b):
    return math.sqrt(a**2 + b**2)

def seno(angulo):
    return math.sin(math.radians(angulo))

def cosseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    return math.tan(math.radians(angulo))

def calcular():
    print("Calculadora de Triangulo Retangulo")
    
    # Escolha da operação
    print("Escolha uma opcao:")
    print("1. Calcular a hipotenusa (Teorema de Pitagoras)")
    print("2. Calcular seno, cosseno ou tangente de um angulo")
    
    opcao = input("Digite 1 ou 2: ")
    
    if opcao == '1':
        a = float(input("Digite o comprimento do cateto a: "))
        b = float(input("Digite o comprimento do cateto b: "))
        hipotenusa = pitagoras(a, b)
        print(f"A hipotenusa é: {hipotenusa:.2f}")
        
    elif opcao == '2':
        angulo = float(input("Digite o ângulo em graus: "))
        print(f"Seno: {seno(angulo):.2f}")
        print(f"Cosseno: {cosseno(angulo):.2f}")
        print(f"Tangente: {tangente(angulo):.2f}")
        
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    calcular()

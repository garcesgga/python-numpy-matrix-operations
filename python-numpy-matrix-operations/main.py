import numpy as np


def matriz():
    x = int(input("Digite o numero de linhas de sua matriz: "))
    y = int(input("Digite o numero de colunas de sua matriz: "))
    mat = np.zeros((x, y))
    for i in range(x):
        for a in range(y):
            num = int(input(f"Digite um numero para sua mnatriz:Linha: {i} Coluna: {a} : "))
            mat[i][a] = num
    return mat


def Opmat():
    matriz1 = matriz()
    matriz2 = matriz()
    soma = matriz1 + matriz2
    mult = matriz1 * matriz2
    print("Soma das  matrizes\n: ", soma)
    print("Multiplicação das matrizes\n: ", mult)
    return soma, mult


def det():
    matriz_1 = matriz()
    trasporta = np.transpose(matriz_1)
    determinante = np.linalg.det(matriz_1)
    print("A tranporta da matriz", trasporta)
    print("O Determinante da Matriz é: ", determinante)
    return trasporta, determinante
def Mult(matriz):
    escalar = int(input("Digite um numero escalar: "))
    result = escalar * matriz
    print("Matriz multiplicada por um escalar", result)
    return result


def menu():
    while True:
        men = int(input("Escolha uma opção\n"
                        "\n1: Criar uma Matriz:"
                        "\n2: Soma e multiplicação de duas matrizes:"
                        "\n3: Transposta de uma matriz, determinante de uma matriz quadrada. "
                        "\n4: Multiplicar uma matriz por um Escalar:"
                        "\n0: Para finalizar o programa: "
                        "\nDigite sua opção:  "))
        if men == 1:
            matriz()
            continue

        elif men == 2:
            Opmat()
            continue

        elif men == 3:
            det()
            continue
        elif men == 4:

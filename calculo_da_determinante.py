# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:55:07 2023

@author: Rebeca
"""

# Definindo a matriz A como uma lista de listas
A = [[1, 2, 3, 4],
     [2, 1, 3, 0],
     [0, 1, 2, -3],
     [-1, 2, 0, 3]]

# Definindo a função para calcular a determinante usando a fórmula dada
def determinant(A):
    # Definindo a variável para armazenar o resultado
    det = 0
    
    # Definindo a função para calcular o sinal de uma permutação
    def signum(p):
        inversions = 0
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if p[i] > p[j]:
                    inversions += 1
        return (-1) ** inversions
    
    # Definindo a função para calcular o produto de uma permutação
    def product(p):
        result = 1
        for i in range(len(p)):
            result *= A[i][p[i]]
        return result
    
    # Gerando todas as permutações da matriz usando a biblioteca itertools
    import itertools
    permutations = itertools.permutations(range(len(A)))
    
    # Somando os produtos das permutações para obter a determinante
    for p in permutations:
        det += signum(p) * product(p)
    
    # Retornando o resultado
    return det

# Chamando a função determinant com a matriz A
det_A = determinant(A)

# Imprimindo o resultado
print('Valor da determinante: ', det_A)

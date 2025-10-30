import numpy as np
# Exercícios Práticos:

# 1. Crie um array de 10 números inteiros e mostre apenas os pares 
    #  - Dica: use indexação booleana com arr % 2 == 0
# print(np.arange(0,21,2))


# 2. Gere uma matriz 3x3 com valores de 1 a 9 e exiba a diagonal principal
    #  - Dica: use np.arange(1, 10).reshape(3, 3) e np.diag()
# matriz = np.arange(1, 10).reshape(3, 3)
# print(matriz)
# print(np.diag(matriz))


# 3. Calcule média, máximo e mínimo de um array de notas
    # Dica: use np.mean(), np.max() e np.min()
# print(np.min(matriz))
# print(np.mean(matriz))
# print(np.max(matriz))


# 4. Crie dois arrays e realize operações matemáticas entre eles
    # Dica: teste soma, subtração, multiplicação e divisão vetorizadas
seq_a = np.arange(1, 11)  # 1 a 10
seq_b = np.arange(11, 21) # 11 a 20

print("Array A:", seq_a)
print("Array B:", seq_b)

print(seq_a + seq_b)
print(seq_a - seq_b)
print(seq_a * seq_b)
print(seq_a / seq_b)

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# print(a + b)
# print(a * b)
# print(b - a)
# print(b / a)



# 5. Gere 50 números igualmente espaçados entre 0 e 5 e mostre o primeiro e último elemento
    # Dica: use np.linspace(0, 5, 50) e indexação [0] e [-1]
# lista = np.linspace(0, 5, 50)
# print(lista)
# print(lista[0])
# print(lista[-1])
'''
2) Construa um programa que calcule a área de um triângulo. O usuário deve fornecer a base e a altura, e o programa deve aplicar a seguinte fórmula: (Valor: 2,0 pontos)
-  Area = (base * altura) / 2
'''
# Requisitando as variáveis necessárias, 'b' de base e 'h' (como a altura é representada na matemática)
b = float(input('Informe a base de um triângulo: '))
h = float(input('Informe a altura de um triângulo: '))

# Saída com o resultado da formula da área do triângulo utilizando as variáveis requisitadas
print('A área desse triângulo é', (b * h) / 2)
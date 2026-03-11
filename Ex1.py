'''
1)  Faça um programa que peça dois números inteiros (X e Y) e um número real (Z). Calcule e mostre: (Valor: 3,0 pontos)
-  O produto do triplo da variável X com o dobro da variável Y.
-  A soma de metade da variável X com a variável Z.
-  A variável Y elevada ao quadrado.
'''

X = int(input('Escolha um número inteiro para a variável X: '))
Y = int(input('Escolha um número inteiro para a variável Y: '))
Z = float(input('Escolha um número inteiro para a variável Z: '))

print('O produto do triplo da variável X com o dobro da variável Y:', (3 * X) * (2 * Y))
print('A soma de metade da variável X com a variável Z:', (X / 2) + Z)
print('A variável Y elevada ao quadrado:', Y**2)
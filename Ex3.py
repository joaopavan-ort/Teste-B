'''
3) Uma empresa de logística cobra uma taxa extra por excesso de peso em encomendas internacionais. Sabendo que a taxa é de R$ 7,50 por quilo excedente, construa um programa que: (Valor: 3,0 pontos)
-  Peça ao usuário para digitar apenas a quantidade de quilos em excesso da encomenda (ex: 2.4).
-  Calcule o valor total da taxa de excesso.
-  Requisito de Saída: Exiba o resultado utilizando Strings Formatadas. O valor da taxa deve aparecer com o símbolo da moeda (R$) e obrigatoriamente com duas casas decimais.
'''

ex = float(input('Quantos quilos em excesso teve a encomenda? '))

print('A taxa para esse pacote é de R${:0.2f}'.format(ex*7.5))
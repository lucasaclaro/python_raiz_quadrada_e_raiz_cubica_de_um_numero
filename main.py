print('***' * 13)
print('Cálculo de raiz quadrada e raiz cúbica')
print('***' * 13)

numero = float(input('\nDigite um número: '))
raiz_quadrada = numero ** (1/2)
raiz_cubica = numero ** (1/3)

print(f'\nA raiz quadrada de {numero:.2f} é {raiz_quadrada:.2f}.')
print(f'A raiz cúbica de {numero:.2f} é {raiz_cubica:.2f}.')
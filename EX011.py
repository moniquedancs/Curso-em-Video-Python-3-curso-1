#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#Entrada dos valores de largura e altura:
l=float(input('Largura da parede, em metros:'))
h=float(input('Altura da parede, em metros:'))

#Variáveis:
area = l*h #cálculo da área de um retângulo (base x altura)
tinta = area/2 #cada litro pinta 2m²

#Saída dos valores de área e litros de tinta necessários:
print('Sua parede possui {:.2f} metros de largura e {:.2f} metros de altura.'.format(l,h))
print('Então, ela possui uma área de {:.2f} m².'.format(area))
print('Você vai precisar de {:.2f} litros de tinta, pois cada litro cobre 2 m².'.format(tinta))
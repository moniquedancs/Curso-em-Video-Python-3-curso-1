#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela.

n=input('Digite algo:')

print('É do tipo primitivo: {}'.format(type(n)))
print('É um número? {}'.format(n.isnumeric()))
print('É um decimal? {}'.format(n.isdecimal()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Possui espaço? {}'.format(n.isspace()))
print('Está em letras minúsculas? {}'.format(n.islower()))
print('Está em letras maiúsculas? {}'.format(n.isupper()))
print('Está capitalizada? {}'.format(n.istitle()))

#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c=float(input('Qual é a temperatura, em graus Celsius?'))
f=c*1.8+32
print('A temperatura {:.1f}ºC equivale a {:.1f}ºF.'.format(c,f))


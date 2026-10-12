#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

#Entrada do valor de temperatura (em ºC):
c = float(input('Qual é a temperatura, em graus Celsius?'))

#Variável de conversão Celsius para Fahrenheit:
f = c*1.8+32

#Saída da temperatura convertida (em ºF):
print('A temperatura {:.1f}ºC equivale a {:.1f}ºF.'.format(c,f))


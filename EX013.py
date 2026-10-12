#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Entrada do valor do salário:
n = float(input('Digite o valor do seu salário:'))

#Variável do cálculo de aumento:
aumento = n*1.15 #Aumento de 15% transformado em número decimal para facilitar os cálculos

#Saída com o valor do salário atualizado com o aumento:
print('Parabéns! Você recebeu um aumento de 15%. Seu salário atual é de {:.2f} reais.'.format(aumento))
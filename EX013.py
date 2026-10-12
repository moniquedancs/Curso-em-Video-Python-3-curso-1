#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n=float(input('Digite o valor do seu salário:'))
aumento=n*1.15
print('Parabéns! Você recebeu um aumento de 15%. Seu salário atual é de {:.2f} reais.'.format(aumento))
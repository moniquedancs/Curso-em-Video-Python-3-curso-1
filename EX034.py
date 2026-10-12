#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

#Entrada do valor do salário:
salario = float(input("Digite o valor do seu salário: "))

#Condição:
if salario > 1250:
    aumento = salario*1.10
else:
    aumento = salario*1.15

#Saída:
print("Com o aumento, seu novo salário será de R${:.2f}. Parabéns!".format(aumento))

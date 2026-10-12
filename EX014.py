#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=float(input('Qual foi a quantidade de quilômetros percorridos?'))
dias=int(input('Qual foi a quantidade de dias de aluguel do carro?'))
kmrodado=km*0.15
carro=dias*60
total=kmrodado+carro
print('Você andou {:.2f} km, por {} dias.'.format(km,dias))
print('O custo de {:.2f} km é de R${:.2f}, pois cada km rodado custa R$0,15.'.format(km,kmrodado))
print('O custo do aluguel do carro por {} dias é de R${:.2f}, pois cada diária custa R$60,00.'.format(dias,carro))
print('O preço total a pagar é de R${:.2f}.'.format(total))
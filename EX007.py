#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Entrada das duas notas:
p1=float(input('Digite sua nota da P1:'))
p2=float(input('Digite sua nota da P2:'))

#Cálculo da variável "média":
media=(p1+p2)/2

#Saída da média:
print('Sua média final foi de {:.2f}.'.format(media))
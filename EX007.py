#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
p1=float(input('Digite sua nota da P1:'))
p2=float(input('Digite sua nota da P2:'))
media=(p1+p2)/2
print('Sua média final foi de {:.2f}.'.format(media))
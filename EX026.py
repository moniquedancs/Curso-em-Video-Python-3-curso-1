#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

#Entrada da frase:
escreva = str(input("Escreva uma frase:")).strip()

#Variável para manipular as letras da frase:
frase = "{}".format(escreva).lower()

#Saída das informações solicitadas:
print("A quantidade de vezes que a letra 'a' aparece é: {}".format(frase.count('a'))) #contar a letra "a"
print("A primeira vez que a letra 'a' aparece é na posição: {}".format(frase.find('a')+1)) #primeira posição da letra "a"
print("A última vez que a letra 'a' aparece é na posição: {}".format(frase.rfind('a')+1)) #última posição da letra "a"

#+1 para ajustar a posição, pois o python começa na posição zero.

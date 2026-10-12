#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras no total (sem espaço).
#Quantas letras tem o primeiro nome.

#Entrada do nome inteiro:
nome = str(input("Digite o seu nome completo:")).strip() #strip remove os espaços em branco no início e no final

#Saída:
print("Seu nome, em letras maiúsculas: {}".format(nome.upper())) #letras maiúsculas
print("Seu nome, em letras minúsculas: {}".format(nome.lower())) #letras minúsculas
print("Seu nome completo tem um total de {} letras.".format(len(nome)-nome.count(" "))) #total de letras
print("Seu primeiro nome tem {} letras.".format(nome.find(" "))) #find(" ") devolve a posição em que o espaço está, ou seja, depois do primeiro nome.
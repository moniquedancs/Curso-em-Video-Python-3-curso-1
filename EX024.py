#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#Entrada do nome da cidade:
n = str(input("Qual é o nome da sua cidade? ")).strip()

#Variável para manipular o nome da cidade, em letras maiúsculas:
ci = str("{}".format(n.upper()))

#Saída com True ou False, a depender se a cidade começa com a palavra Santo:
print("Sua cidade começa com o nome 'Santo': (True = Sim / False = Não)")
print(ci[:5] == 'SANTO')

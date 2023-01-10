import os
os.system('cls')

nome = []
raca = []
idade = []
i = int(input('Quantos animais serão fornecidos?\n'))
k = a = b = c= 0

while k < i:
    os.system('cls')
    cachorro = input('Forneça o nome do cachorro: ')
    nome.append(cachorro)
    k+=1

print('Agora vamos ver a raça dos fofuxos!')

while a < i:
    os.system('cls')
    cachorro = input('Forneça a raça de %s: ' % nome[a])
    raca.append(cachorro)
    a+=1

print('Agora forneça a idade dos peludos!')

while b < i:
    os.system('cls')
    cachorro = input('Forneça a idade de %s: ' % nome[b])
    idade.append(cachorro)
    b+=1

os.system('cls')

while c < i:
    print('| Nome: ' + nome[c] + ' |' + ' Raça: ' + raca[c] + ' |' + ' Idade: ' + idade[c] + ' |')
    c+=1

input('Digite enter para finalizar.')
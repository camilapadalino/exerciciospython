nome = input('Insira seu nome: ')
print(f'Seja bem vindo(a) {nome}!')
peso = int(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
IMC = peso / altura**2
print('Agora vamos calcular seu IMC')
print(f'Seu IMC (Índice de Massa Corpórea) é igual a {IMC}')
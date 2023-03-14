nome = input('Insira seu nome:')
carros = int(input('Insira o número de carros vendidos:'))
salario1 = 2500.00
valor = float(input('Insira o valor total de vendas:'))
comissao = 200.00 * carros
porcentagem = 0.02 * valor
salariototal = salario1 + comissao + porcentagem
print(f'Nome do vendedor: {nome} \n Número de carros vendidos: {carros} \n Valor toal das vendas: {valor} \n O vendedor {nome} receberá um salário de R$ {salariototal}')
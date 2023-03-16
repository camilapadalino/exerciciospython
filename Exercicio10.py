numero = int(input('Insira um número com 3 dígitos: '))
a = numero%100
b = numero//100
c= a//10
d = a%10
e = (d*100)+(c*10)+ b
print (e)
#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input('Entre com a quantidade de dias: '))
horas = int(input('Entre com a quantidade de horas: '))
minutos = int(input('Entre com a quantidade de minutos '))
segundos = int(input('Entre com a quantidade de segundos '))
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print('O tempo total em segundos que você digitou é: {}'.format(total_em_segundos))

import math

# desenvolva um programa que peça dois numeros inteiros e imprima a divisão inteira do primeiro pelo segundo
'''
num1 = int (input("Digite o primeiro número inteiro: "))
nun2 = int(input("Digite o segundo número inteiro: "))

print(f"A divisão inteira de {num1} por {nun2} é: {num1 // nun2}.")
'''

# escreva um programa que calcule a area do circulo recebendo o raio como entrada

'''raio = float(input("Digite o raio do círculo: "))
area_do_circulo = math.pi * (raio ** 2)
print(f"A área do círculo com raio de {raio} é: {area_do_circulo:.2f}.")
'''
# Faça um programa que peça para o usuário digitar uma data no formado dd/mm/aaaa e imprima o dia, o mês e o ano separados.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split('/')
print(f"O dia é: {dia}, o mês é: {mes} e o ano é: {ano}.")
import math

# desenvolva um programa que peça dois numeros inteiros e imprima a divisão inteira do primeiro pelo segundo
'''try:
    num1 = int (input("Digite o primeiro número inteiro: "))
    nun2 = int(input("Digite o segundo número inteiro: "))
    print(f"A divisão inteira de {num1} por {nun2} é: {num1 // nun2}.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de digitar dois números inteiros.")    '''

# escreva um programa que calcule a area do circulo recebendo o raio como entrada

'''raio = float(input("Digite o raio do círculo: "))
area_do_circulo = math.pi * (raio ** 2)
print(f"A área do círculo com raio de {raio} é: {area_do_circulo:.2f}.")
'''
# Faça um programa que peça para o usuário digitar uma data no formado dd/mm/aaaa e imprima o dia, o mês e o ano separados.

'''data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split('/')
print(f"O dia é: {dia}, o mês é: {mes} e o ano é: {ano}.")'''


numero = 33
if isinstance(numero, int):
        print(f" a variavel {numero} é um inteiro.")
else:
        print(f"a variavel {numero} não é um inteiro.")
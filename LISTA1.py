'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    print('Samuel Pineli')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    produto = 30 * 27
    print(produto)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    soma = 5+8+12
    print(soma/3)

#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    num = int(input('Digite um numero inteiro:'))
    print(num)

#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num = float(input('Digite um numero real:'))
    num2 = float(input('Digite dois numero real:'))
    print(num)
    print(num2)

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    num = int(input('Digite um numero inteiro:'))
    num2 = num -1
    print(num2)

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = (input('Digite seu nome:'))
    endereco = (input('Digite seu endereço:'))
    telefone = (input('Digite telefone:'))
    print(f'O nome do cliente é: {nome}')
    print(f'O endereço do cliente é :{endereco}')
    print(f'O telefone do cliente é: {telefone}')

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    num = int(input('Digite um numero inteiro:'))
    num2 = int(input('Digite um numero inteiro:'))
    num3 = num - num2
    print(num3)

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input('Digite um numero real:'))
    num2 = num/4
    print(num2)
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('Digite um numero real:'))
    num2 = float(input('Digite um numero real:'))
    num3 = float(input('Digite um numero real:'))
    media = num1 + num2 + num3/3

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = float(input('1 Número:'))
    num2 = float(input('2 Número:'))
    print(f'{num1} + {num2} = {round(num1+num,2)}')
    print(f'{num1} + {num2} = {round(num1-num,2)}')
    print(f'{num1} + {num2} = {round(num1*num,2)}')
    print(f'{num1} + {num2} = {round(num1/num,2)}')


#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    numero = float(input('Digite um número real:'))
    print(numero*numero)

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = round(float(input('Digite o saldo da conta poupança:R$')),2)
    print(f'O novo saldo da conta poupaça é:{round(saldo*1.02,2)}')

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura / 2).
def q14():

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.

q9()
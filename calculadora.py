'''Essa calculadora foi feita por mim no 1º termo da faculdade
onde eu precisava resolver mais rapidamente os calculos de determinantes de matrizes
que eram em grandes quantidades, então para ela não ficar somente com isso eu add os outros calculos tambem, ela é simples, não tem design
pois foi só para resolver meus problemas de matrizes kkkk'''

import numpy
resposta = 's'
while resposta.lower() == 's':
    print('Qual tipo de conta você deseja fazer? Leia as opções abaixo')
    print('-'*30)
    print('Digite + para soma')
    print('Digite - para subtração')
    print('Digite X para multiplicação')
    print('Digite / para divisão')
    print('Digite Det para Determinante de matrizes')
    print('Digite XX para exponenciação')
    op = str(input())


    print('-'*30)

    if op.lower() == '+':
        print('Digite um número')
        n1 = float(input())
        print('Digite outro número')
        n2 = float(input())
        soma = n1+n2
        print('O resultado é: %1.2f'%(soma))    

    elif op.lower() == '-':
        print('Digite um número')
        n1 = float(input())
        print('Digite outro número')
        n2 = float(input())   
        sub = n1-n2
        print('O resultado é: %1.2f'%(sub))
    
    elif op.lower() == 'x':
        print('Digite um número')
        n1 = float(input())
        print('Digite outro número')
        n2 = float(input())
        mult = n1*n2
        print('O resultado é: %1.2f'%(mult))
    elif op.lower() == '/':
        print('Digite um número')
        n1 = float(input())
        print('Digite outro número')
        n2 = float(input())
        div = n1/n2
        print('O resultado é: %1.2f'%(div))
    elif op.lower() == 'det':
        matriz = []
        print('Quantas colunas terá sua matriz? ')
        coluna = int(input())

        print('Quantas linhas terá sua matriz? ')
        linha = int(input())

        for i in range(coluna):
            matriz.append([])

            for j in range(linha):
                matriz[i].append(int(input('Digite um valor [{}] [{}] -> '.format(i,j))))

        det = numpy.linalg.det(matriz)
        print('A matriz escolhida foi: ')
        print(matriz)
        print('O determinante é: %1.2f'%(det))
    elif op.lower() == 'xx':
        print('Digite o número da base')
        n1 = float(input())
        print('Elevado a quanto?')
        n2 = float(input())
        expon = n1**n2
        print('O resultado da exponenciação é %1.2f'%(expon))
    
    else:
        print('Digite um operador valido, igual está pedindo acima!')
    print('Deseja fazer outra operação? (S/N)')
    resposta = str(input())
    print('FIM!')

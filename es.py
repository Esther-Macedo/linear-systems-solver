from Sistema import Sistema

#funções que lidam com entrada e saida 

def preencher_coeficientes (sistema: Sistema):
        '''captura entrada de coeficientes do usuário'''
        a = []
        n = int(input())
        for i in range(n):
            linha = list(map(float, input().split()))
            a.append(linha)
        sistema.a_original = a
        sistema.a = a

def preencher_constantes (sistema: Sistema):
    '''captura entrada de coeficientes do usuário'''
    c = []
    n = int(input())
    for i in range (n):
        constante = float(input())
        c.append(constante)
    sistema.c_original = c
    sistema.c = c

def sinal(n: float, first:bool = False)-> int: 
    '''Extrai sinal de um numero e retorna sinal e numero como string, omitindo o sinal de positivo ou o espaço entre o sinal negativo e numero a depender da posição'''
    if n<0 and first:
        return f'-{abs(n):.2f}'
    elif n<0 and not first :
        return f'- {abs(n):.2f}'
    elif n>=0 and not first:
      return f'+ {abs(n):.2f}'  
    return f'{abs(n):.2f}'


def imprimir_sistema(sistema: Sistema):
    '''imprime sistema com os dados imputados pelo comando a e s'''
    
    n= sistema.tam()
    for i in range (n):
        linha=f'{sinal(sistema.a_original[i][0],True)} x{1}'
        for j in range(1,n):
            linha+=f' {sinal(sistema.a_original[i][j])} x{j+1}'
        
        
        linha+=f' = { sinal(sistema.c_original[i],True)}'
        print(linha)

def imprimir_solucao(sistema: Sistema):
    '''imprime vetor x do sistema'''
    if sistema.x and len(sistema.x)>0:
        for i in range(len(sistema.x)):
            print(f'x{i+1}: {sistema.x[i]: .2f}')

def imprimir_matriz(lista: list,label = None):
    '''imprime  de uma lista de lista'''
    if label:
        print(label)
    tam = len(lista)
    for linha in lista:
        print(" ".join(f'{n:.2f}' for n in linha ))
        
            
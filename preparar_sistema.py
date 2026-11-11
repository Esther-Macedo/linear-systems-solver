
def preencher_coeficientes (coeficientes:list):
    '''captura entrada de coeficientes do usuário'''

    n = int(input())
    for i in range(n):
        linha = list(map(float, input().split()))
        coeficientes.append(linha)

def preencher_constantes (constantes: list):
    '''captura entrada de coeficientes do usuário'''
    n = int(input())
    for i in range (n):
        constante = float(input)
        constantes.append(constante)


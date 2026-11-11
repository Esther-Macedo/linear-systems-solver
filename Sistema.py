from utilitarios import sinal

class Sistema:

    def __init__(self):
        self.coeficientes = []
        self.constantes = []
        self.solucao = []

    def set_coeficientes(self, c:list):
        self.coeficientes = c

    def set_constantes(self, c:list):
        self.constantes = c
    
    def get_coef(self)->list:
        '''retorna coeficientes'''
        return self.coeficientes

    def get_const(self)-> list:
        return self.coeficientes
    
    def achar_linha_max_coluna_0(self):
        '''retorna a linha do maior numero da coluna 0 da matriz de coeficientes'''
        primeiros = []
        for i in range (len(self.constantes)):
            primeiros.append(self.coeficientes[0][i])
        maximo= max(primeiros)
        pos= primeiros.index(maximo)
        return pos


    def trocar_linhas(self, l1:int, l2:int):
        '''Troca linhas da matriz de coeficientes e do vetor de constantes'''
        if l1 < len(self.coeficientes)> l2:
            self.coeficientes[l1],self.coeficientes[l2]=self.coeficientes[l2],self.coeficientes[l1]
            self.constantes[l1],self.constantes[l2]=self.constantes[l2],self.constantes[l1]

    def preencher_coeficientes (self):
        '''captura entrada de coeficientes do usuário'''

        n = int(input())
        for i in range(n):
            linha = list(map(float, input().split()))
            self.coeficientes.append(linha)

    def preencher_constantes (self):
        '''captura entrada de coeficientes do usuário'''
        n = int(input())
        for i in range (n):
            constante = float(input())
            self.constantes.append(constante)

    def imprimir(self):
        '''imprime sistema'''
        
        for i in range (len(self.coeficientes)):
            linha=f'{sinal(self.coeficientes[i][0],True)} x{1}'
            for j in range(1,len(self.coeficientes)):
                linha+=f' {sinal(self.coeficientes[i][j])} x{j+1}'
            
            
            linha+=f' = { sinal(self.constantes[i],True)}'
            print(linha)
        

from dataclasses import dataclass

@dataclass
class Sistema:
    '''Classe para guardar valores dos sistema'''
    a_original: list
    c_original: list
    a: list #copia da matriz de coeficientes
    c: list
    x: list #solução
    l: list #matriz L
    u: list #matriz U
    solved: bool = False #marca se um sistema já passou por aluguma solução

    def inicializar_vetor_solucao(self):
        '''inicializa vetor solução com 0 e tamanho correspontendo ao tamanho do sistema'''
        self.x = [0]*(self.tam()) 


    def tam(self)-> int: 
        '''retorna tamanho do sistema. Como o sistema será sempre quadrado retorna o nº de colunas'''
        return len(self.a)
            
    def posicao_coef_max_coluna_0(self)->int:
        '''retorna a linha do maior numero da coluna 0 da matriz de coeficientes'''
        primeiros = []
        for i in range (self.tam):
            primeiros.append(self.a[0][i])
        maximo= max(primeiros)
        pos= primeiros.index(maximo)
        return pos


    def trocar_linhas(self, l1:int, l2:int):
        '''troca linhas da matriz de coeficientes e do vetor de constantes'''
        if l1 < len(self.coeficientes)> l2:
            self.a[l1],self.a[l2]=self.a[l2],self.a[l1]
            self.c[l1],self.c[l2]=self.c[l2],self.c[l1]

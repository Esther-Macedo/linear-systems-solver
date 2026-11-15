from dataclasses import dataclass

@dataclass
class Sistema:
    '''Classe para guardar valores dos sistema'''
    a: list 
    c: list
    x: list
    l: list #matriz L
    u: list #matriz U
    resolvido: bool = False #marca se o sistema já foi resilvido

    def inicializar_vetor_solucao(self):
        '''inicializa vetor solução com 0 e tamanho correspondendo ao tamanho do sistema'''
        self.x = [0]*(self.tam()) 

    def inicializar_matriz_l(self):
        '''inicializa a matriz L como uma matriz identidade'''
        tam = self.tam()
        self.l=[]
        for i in range(tam):
            linha=[0]*tam
            linha[i]=1
            self.l.append(linha)


    def tam(self)-> int: 
        '''retorna tamanho do sistema. Como o sistema será sempre quadrado retorna o nº de linhas'''
        return len(self.a)

            
    def posicao_coef_max_coluna(self, linha_inicial:int, coluna:int )->int:
        '''retorna a linha do maior coeficiente em módulo de uma subcoluna da matriz de coeficientes'''

        if linha_inicial< self.tam():
            coeficientes_coluna = []
            #começa a apartir da linha passada como parametro
            for i in range (linha_inicial, self.tam()): 
                 #coleta os coeficientes da coluna
                coeficientes_coluna.append(abs(self.a[i][coluna]))
        
            maximo= max(coeficientes_coluna)
            pos= coeficientes_coluna.index(maximo)
    
            return pos+linha_inicial


    def trocar_linhas(self, l1:int, l2:int):
        '''troca linhas da matriz de coeficientes e do vetor de constantes'''
        if l1 < len(self.a)> l2:
            self.a[l1],self.a[l2]=self.a[l2],self.a[l1]
            self.c[l1],self.c[l2]=self.c[l2],self.c[l1]

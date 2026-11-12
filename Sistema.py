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
        '''inicializa vetor solução com 0 e tamanho correspondendo ao tamanho do sistema'''
        self.x = [0]*(self.tam()) 

    def inicializar_matriz_l(self):
        '''inicializa a matriz L'''
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
        '''retorna a linha do maior numero de uma subcoluna da matriz de coeficientes'''
        print(f'linha_inicial: {linha_inicial}')
        print(f'coluna: {coluna}')
        if linha_inicial< self.tam():
            primeiros = []
            for i in range (linha_inicial, self.tam()):
                primeiros.append(abs(self.a[i][coluna]))
            print(f'coletados:{primeiros}')
            maximo= max(primeiros)
            print(f'max:{maximo}')

            pos= primeiros.index(maximo)
            print(f'pos: {pos}')
            return pos+linha_inicial


    def trocar_linhas(self, l1:int, l2:int):
        '''troca linhas da matriz de coeficientes e do vetor de constantes'''
        if l1 < len(self.a)> l2:
            self.a[l1],self.a[l2]=self.a[l2],self.a[l1]
            self.c[l1],self.c[l2]=self.c[l2],self.c[l1]

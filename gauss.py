##funções de solução por eliminação de gauss 
from Sistema import Sistema
import es

def pivoteamento_parcial(sistema:Sistema, linha_pivo:int):
    '''efetua a troca de linhas do pivoteamento parcial'''
    
    #checa a linha onde está o maior numero da coluna 
    linha_maior= sistema.posicao_coef_max_coluna(linha_pivo, linha_pivo)
   
    #se a linha diferente do que 
    if linha_pivo != linha_maior:
        sistema.trocar_linhas(linha_pivo, linha_maior)
        

def eliminacao(sistema: Sistema, isParcial: bool = False, isFatoracao:bool = False):
    '''faz a eliminação de gauss ou preenche a matriz L dependo dos parametros'''

    tamanho = sistema.tam()
    
    
    for linha_pivo in range(tamanho-1):
        

        if isParcial:
            pivoteamento_parcial(sistema,linha_pivo)

        
        for  i in range (linha_pivo+1,tamanho):
    
            #calcula multiplicador
            m = sistema.a[i][linha_pivo]/sistema.a[linha_pivo][linha_pivo]

            if isFatoracao:
                #preeenche a matriz L com os multiplicadores caso 
                sistema.l[i][linha_pivo]=m

            #faz a operação de linhas Li - m*Lpivô 
            for j in range(linha_pivo, tamanho):
                sistema.a[i][j]= sistema.a[i][j] - m*sistema.a[linha_pivo][j]

            #faz o peração de linha no vetor de constantes se não for fatoração LU
            if not isFatoracao:
                sistema.c[i]= sistema.c[i] - m*sistema.c[linha_pivo]


def resolver(sistema: Sistema):
    '''calcula lista de solução de um sistema triangular'''
    
    if sistema.resolvido:

        tam = sistema.tam()      
        sistema.inicializar_vetor_solucao()
        #acessa matriz de baixo pra cima para comecar do ultimo x
        for i in range(tam-1, -1, -1):
            
            sum=0
            for j in range(tam-1,i,-1):
        
                #substituição dos valores xn já descobertos da linha e soma 
                sum+= sistema.a[i][j]*sistema.x[j]
                

            #isola o xi
            sistema.x[i]= (sistema.c[i]-sum)/sistema.a[i][i]


def gauss(sistema: Sistema):
    
    eliminacao(sistema)
    sistema.resolvido = True
    resolver(sistema)
    es.imprimir_solucao(sistema)

def gauss_parcial(sistema: Sistema):
    
    eliminacao(sistema,True)
    sistema.resolvido=True
    resolver(sistema)
    es.imprimir_solucao(sistema)
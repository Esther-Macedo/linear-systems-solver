##funções de solução por eliminação de gauss 
from Sistema import Sistema
import es

def eliminacao(sistema: Sistema, isConstantes:bool = True, isFatoracao = False):
    '''faz a eliminação de gauss ou preenche a matriz L dependo dos parametros'''

    tamanho = sistema.tam()
    print('in elimination')
    
    for linha_pivo in range(tamanho-1):
        print('linha do pivo: ', linha_pivo )
        
        for  i in range (linha_pivo+1,tamanho):
            print(i)
            print(sistema.a)
            print(sistema.c)
            m = sistema.a[i][linha_pivo]/sistema.a[linha_pivo][linha_pivo]

            if isFatoracao:
                sistema.l[i][linha_pivo]=m

            for j in range(linha_pivo, tamanho):
                sistema.a[i][j]= sistema.a[i][j] - m*sistema.a[linha_pivo][j]

            if isConstantes:
                sistema.c[i]= sistema.c[i] - m*sistema.c[linha_pivo]
    print('A:')
    print(sistema.a)
    print('C:')
    print(sistema.c)


def eliminacao_pivoteamento_parcial(sistema: Sistema):
    '''executa eliminação de gauss com pivoteamento parcial'''


def solve(sistema: Sistema):
    '''calcula lista de solução do sistema'''
    print('in solve')
    if sistema.solved:

        tam = sistema.tam()      
        sistema.inicializar_vetor_solucao()
        # sistema.x[tam-1]= sistema.c[tam-1]/sistema.a[tam-1][tam-1]
    
       
    
        if sistema.solved:
            for i in range(tam-1, -1, -1):
                print('na linha:', i)
                sum=0
                for j in range(tam-1,i,-1):
                    print('na coluna', j)
                    sum+= sistema.a[i][j]*sistema.x[j]
                    print(sum)
    
                sistema.x[i]= (sistema.c[i]-sum)/sistema.a[i][i]
    print(sistema.x)

           

# def solve_recursivo(sistema: Sistema, i:int):
#     sum=0
#     if i == sistema.tam() - 1:
#         sistema.x[i] = sistema.c[i]/sistema.a[i][i]

#     elif i >= 0:
#         sum+=solve_recursivo(sistema, i-1)
#         x[i]= 


def gauss(sistema: Sistema):
    print('in gauss')

    eliminacao(sistema)
    sistema.solved = True
    solve(sistema)
    print('A')
    print(sistema.a)
    es.imprimir_solucao(sistema)






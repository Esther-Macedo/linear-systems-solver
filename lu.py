from Sistema import Sistema
from gauss import eliminacao
import es 

def lu(sistema: Sistema):
    #inicializa matriz L
    sistema.inicializar_matriz_l()
    #chama eliminação sem pivoteamento parcial, e passando o booleano de fatoração como true
    eliminacao(sistema,False,True)
    sistema.u = sistema.a
    es.imprimir_matriz(sistema.u, 'U:')
    es.imprimir_matriz(sistema.l,'L:')
    





from Sistema import Sistema
from gauss import eliminacao
import es 

def lu(sistema: Sistema):
    print("implementar lu")
    sistema.inicializar_matriz_l()
    eliminacao(sistema,False,True)
    sistema.u = sistema.a

    es.imprimir_matriz(sistema.u, 'U:')
    es.imprimir_matriz(sistema.l,'L:')
    





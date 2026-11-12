from Sistema import Sistema
from gauss import gauss, gauss_pivoteamento_parcial
from lu import lu
import es

def main():
    '''função principal do programa'''
    sistema = Sistema.__new__(Sistema)


    running = True

    

    while running:
        comando = input()

        match comando:
            case 'a':
                es.preencher_coeficientes(sistema)   
            case 'c':
                es.preencher_constantes(sistema)
            case 'p':
                es.imprimir_sistema(sistema)
            case 's':
                gauss(sistema)
            case 'r':
                gauss_pivoteamento_parcial(sistema)
            
            case 'l':
                lu(sistema)

            case 'e':
                running = False
                break


if __name__ == '__main__':
    main()

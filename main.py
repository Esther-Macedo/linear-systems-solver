from Sistema import Sistema
from gauss import gauss
from gauss_pivoteamento_simples import gauss_pivoteamento_simples
from lu import lu

def main():
    '''função principal do programa'''
    sistema = Sistema()


    running = True

    sistema =  Sistema()

    while running:
        comando = input();

        match comando:
            case 'a':
                sistema.preencher_coeficientes()
            case 'c':
                sistema.preencher_constantes()
            case 'p':
                sistema.imprimir()
            case 's':
                gauss(sistema)
            case 'r':
                gauss_pivoteamento_simples(sistema)
            
            case 'l':
                lu(sistema)

            case 'swap':
                sistema.trocar(1,2)
            case 'e':
                running = False
                break


if __name__ == '__main__':
    main()

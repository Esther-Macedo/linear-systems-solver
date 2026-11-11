#funções diversas

def sinal(n: float, first:bool = False)-> int: 
    '''Extrai sinal de um numero e retorna sinal e numero como string, omitindo o sinal de positivo ou o espaço entre o sinal negativo e numero a depender da posição'''
    if n<0 and first:
        return f'-{abs(n):.2f}'
    elif n<0 and not first :
        return f'- {abs(n):.2f}'
    elif n>=0 and not first:
      return f'+ {abs(n):.2f}'  
    return f'{abs(n):.2f}'


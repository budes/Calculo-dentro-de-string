def Formata(calc):
    # Resultado final
    resultado = []
    
    # As operações indicadas
    op = ['+', '-', '*', '/'] 

    # ----- A FORMATAÇÃO -----

    aux = ''
    for elemento in calc:
        # Se o elemento for um operador
        if elemento in op:
            resultado.append(aux)           # Adiciona o auxiliar
            resultado.append(elemento)      # Adiciona o operador
            aux = ''                        # Reseta o auxiliar

        # Se não for
        else:
            aux += elemento

    resultado.append(aux)  # Coloquei para evitar perda de dados no final

    return resultado

def Calcula(calc_formatado):
    op = ['+', '-', '*', '/'] # Operadores
    
    if calc_formatado[1] not in '/*':
        resultado = int(calc_formatado[0]) # Recebe o primeiro valor indicado
    else:
        resultado = 0

    # ----- EXECUTA A OPERAÇÃO -----

    for turno in range(0, 2):
        for i, elemento in enumerate(calc_formatado):
            
            if turno == 0 and elemento in '*/': # Ocorre antes da soma e subtração

                aux = 0 # Variável auxiliar que vai receber a divisão ou multiplicação

                if elemento == '*':
                    aux = int(calc_formatado[i-1]) * int(calc_formatado[i+1])

                if elemento == '/':
                    # Faz divisão inteira pra prevenir valores quebrados (1.23, por exemplo)
                    aux = int(calc_formatado[i-1]) // int(calc_formatado[i+1]) 
        

                # Apaga os valores e modifica na lista do cálculo, para que a soma ocorra normal
                for apaga in range(3): calc_formatado.pop(i-1) 
                calc_formatado.insert(i-1, str(aux)) 
                
                if resultado == 0 and i == 1: # Caso a divisão/multiplicação ocorra no início
                    resultado = aux


            elif turno == 1 and elemento in '+-': # Ocorre depois da divisão e multiplicação
                
                if elemento == '+':
                    resultado += int(calc_formatado[i+1])

                if elemento == '-':
                    resultado -= int(calc_formatado[i+1])


    return resultado

calculo = '42/2+38-123*5'

print('Valor obtido pelo código:', Calcula(Formata(calculo)))
print('Valor obtido pelo eval:', eval(calculo))

# Calculo-dentro-de-string
Faz um cálculo dentro de uma string sem usar eval

# Operadores indicados

• Soma e subtração.

• Divisão e multiplicação.

# Etapas
### • Fazer as operações.

## Formatar o cálculo indicado

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

            
op → Lista de operadores que podem ser usados

Ele faz uma divisão da string e coloca numa lista chamada resultado.

Para isso ele vai colocando cada um dos valores obtidos na variável aux, 
quando um valor é um dos operadores ele adiciona o valor pra lista, adiciona
o operador também e reseta a variável aux.

Ao final, para evitar perdas coloquei para adicionar o resto do auxiliar para
dentro do resultado.

O **output** gerado segue essa **estrutura**: '1+1' → ['1', '+', '1']


## Fazer as operações

    resultado = int(calc_formatado[0]) # Recebe o primeiro valor indicado
 
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

            elif turno == 1 and elemento in '+-': # Ocorre depois da divisão e multiplicação
                
                if elemento == '+':
                    resultado += int(calc_formatado[i+1])

                if elemento == '-':
                    resultado -= int(calc_formatado[i+1])
                    
                    
O sistema, embora grandinho é simples, ele simplesmente adiciona já de início um valor para dentro do resultado
esse valor é o primeiro valor do cálculo, ele faz isso para que já tenha um valor inicial definido.

Ao seguir, o for divide em turnos pois divisão e multiplicação tem ordem de prescedência diferente da soma e 
subtração.

### Turno 0

Quando segue mais adiante, caso o turno seja o 0, ele adiciona para a auxiliar o resultado da divisão/multiplicação 
no lugar dos valores anteriores, pois para que a soma e subtração ocorra adequadamente ele precisa dos números dispostos
corretamente, para isso ele apaga os elementos anteriores e insere a auxiliar. 

### Turno 1

Quando entrar no turno 1, ele só adiciona ao resultado o valor que for indicado para o resultado, com a operação indicada.

Por último, retorna o resultado

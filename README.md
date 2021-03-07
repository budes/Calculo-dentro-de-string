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
            
op → Lista de operadores que podem ser usados

Ele faz uma divisão da string e coloca numa lista chamada resultado.

Para isso ele vai colocando cada um dos valores obtidos na variável aux, 
quando um valor é um dos operadores ele adiciona o valor pra lista, adiciona
o operador também e reseta a variável aux.

O **output** gerado segue essa **estrutura**: '1+1' → ['1', '+', '1']

import ply.lex as lex
 

 # ------------------------------------------------------------
 # 
 # Parte de Analise Sintatica 
 # 
 # ------------------------------------------------------------

import ply.yacc as yacc

def p_expr_add(p):
    'expr : name OPERADOR_ATRIBUICAO factor OPERADOR_SOMA factor PONTO_VIRGULA'
    return 'Sintaxe Correta \n'

def p_expr_sub(p):
    'expr : name OPERADOR_ATRIBUICAO factor OPERADOR_SUBTRACAO factor PONTO_VIRGULA'
    return 'Sintaxe Correta \n'

def p_expr_mul(p):
    'expr : name OPERADOR_ATRIBUICAO factor OPERADOR_MULTIPLICACAO factor PONTO_VIRGULA'
    return 'Sintaxe Correta \n'

def p_expr_div(p):
    'expr : name OPERADOR_ATRIBUICAO factor OPERADOR_DIVISAO factor PONTO_VIRGULA'
    return 'Sintaxe Correta \n'

def p_factor_real(p):
    'factor : NUMERO_REAL'  # Aceita 12.5
    return 'Sintaxe Correta \n'

def p_factor_int(p):
    'factor : NUMERO_INTEIRO'  # Aceita 12.5
    return 'Sintaxe Correta \n'

def p_name(p):
    'name : IDENTIFICADOR'  # Aceita 12.5

# Error rule for syntax errors
def p_error(p):
    print("Erro de Sintaxe")

# Build the parser
parser = yacc.yacc()

def sintatic_analysis(): 
    result = parser.parse(my_text.get(1.0, END))
    # my_terminal.insert(END, result)
    print(type(result))


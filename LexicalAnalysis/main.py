import ply.lex as lex

 # ------------------------------------------------------------
 # 
 # Parte de Analise Lexica 
 # 
 # ------------------------------------------------------------

import ply.yacc as yacc
tokens = [
    'NUMERO_REAL',
    'OPERADOR_SOMA',
    'OPERADOR_SUBTRACAO',
    'OPERADOR_MULTIPLICACAO',
    'OPERADOR_DIVISAO',
    'OPERADOR_ATRIBUICAO',
    'PONTO_VIRGULA',
    'IDENTIFICADOR',
    'NUMERO_INTEIRO'
]

reserved = {
    'if' : 'PALAVRA RESERVADA - IF',
    'then' : 'PALAVRA RESERVADA - THEN',
    'else' : 'PALAVRA RESERVADA - ELSE',
    'while' : 'PALAVRA RESERVADA - WHILE',
    'program' : 'PALAVRA RESERVADA - PROGRAM',
    'procedure' : 'PALAVRA RESERVADA - PROCEDURE',
    'var' : 'PALAVRA RESERVADA - VAR',
    'int' : 'PALAVRA RESERVADA - INT',
    'boolean' : 'PALAVRA RESERVADA - BOOLEAN',
    'read' : 'PALAVRA RESERVADA - READ',
    'write' : 'PALAVRA RESERVADA - WRITE',
    'true' : 'PALAVRA RESERVADA - TRUE',
    'false' : 'PALAVRA RESERVADA - FALSE',
    'begin' : 'PALAVRA RESERVADA - BEGIN',
    'end' : 'PALAVRA RESERVADA - END',
    'do' : 'PALAVRA RESERVADA - DO',
    'and' : 'PALAVRA RESERVADA - AND',
    'not' : 'PALAVRA RESERVADA - NOT',
    'or' : 'PALAVRA RESERVADA - OR',
 }
 
 # Regular expression rules for simple tokens
t_OPERADOR_SOMA = r'\+'
t_OPERADOR_SUBTRACAO = r'-'
t_OPERADOR_MULTIPLICACAO   = r'\*'
t_OPERADOR_DIVISAO  = r'/'
t_OPERADOR_ATRIBUICAO  = r'\:='
t_PONTO_VIRGULA  = r';'

 # A regular expression rule with some action code
def t_NUMERO_REAL(t):
    r'([0-9]*)\.([0-9]*)'
    t.value = float(t.value)    
    return t

def t_NUMERO_INTEIRO(t):
    r'\d+'
    if len(str(t.value)) <= 30:
        return t
    else:
        return print("Valor do inteiro muito grande: ", t.value)

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'IDENTIFICADOR')    # Check for reserved words
     return t

 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def find_column(self, token):
	line_start = self.input.rfind('\n', 0, token.lexpos) + 1
	return (token.lexpos - line_start) + 1
 
 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
    my_terminal.insert(END, "Caracter invalido --------- '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'//.*|{[\s\S]*}'
    pass

lexer = lex.lex()

# Lexical analysis
def lexical_analysis():
    lexer.input(my_text.get(1.0, END))
    
    while True:
        tok = lexer.token()
        if not tok: 
            break
        my_terminal.insert(END, '\n' + tok.value + '---------' + tok.type)
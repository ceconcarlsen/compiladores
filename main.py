 # ------------------------------------------------------------
 # 
 # Parte de Analise Lexica 
 # 
 # ------------------------------------------------------------
import ply.lex as lex
 
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Compiladores')
root.geometry('1260x660')

# Set variable for open file name 
global open_status_name
open_status_name = False

# Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Textbox
my_text = Text(my_frame, width=97, height=18, font=(
    "Helvetica", 16), selectbackground="blue",
    selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

my_terminal = Text(my_frame, width=97, height=7, font=(
    "Helvetica", 16), selectbackground="blue",
    selectforeground="black", undo=False, yscrollcommand=text_scroll.set)
my_terminal.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)
text_scroll.config(command=my_terminal.yview)

 # List of token names.   This is always required
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

 # ------------------------------------------------------------
 # 
 # Parte de Analise Lexica 
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



 # ------------------------------------------------------------
 # 
 # Parte do UI - TKINTER 
 # 
 # ------------------------------------------------------------

# Create New File 
def new_file():
    my_text.delete("1.0", END)
    root.title('Novo arquivo - Compiladores')
    status_bar.config(text="Novo arquivo   ")

# Open Files
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Abrir arquivo", filetypes=(("Text Files", "*.txt"),)) 
    if text_file:
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text=f'{name}         ')
    name = name.replace("C:/", "")
    root.title(f'{name}')
    # Open the file 
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox 
    my_text.insert(END, stuff)
    # Close the opened file 
    text_file.close()

# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir="C:/", title="Salvar o arquivo", filetypes=(("Text Files", "*.txt"),))
    if text_file: 
        # Update Status Bars 
        name = text_file
        status_bar.config(text=f'{name}              ')
        name = name.replace('C:/', "")
        root.title(f'{name} - Compilador')

        # Salvar o arquivo 
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the opened file 
        text_file.close()

# Save file 
def save_file():
    global open_status_name
    if open_status_name:
        # Salvar o arquivo 
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the opened file 
        text_file.close()
        # Put status update or popup code
        status_bar.config(text=f'Salvo: {open_status_name}              ')
    else: 
        save_as_file()

lexer = lex.lex()

# Lexical analysis
def lexical_analysis():
    lexer.input(my_text.get(1.0, END))
    
    while True:
        tok = lexer.token()
        if not tok: 
            break
        my_terminal.insert(END, '\n' + tok.value + '---------' + tok.type)

def sintatic_analysis(): 
    result = parser.parse(my_text.get(1.0, END))
    # my_terminal.insert(END, result)
    print(type(result))

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="Arquivo", menu=file_menu)
my_menu.add_command(label="Analisador lexico", command=lexical_analysis)
my_menu.add_command(label="Analisador sintatico", command=sintatic_analysis)
file_menu.add_command(label="Novo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_command(label="Salvar como...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)

# Add Status Bar
status_bar = Label(root, text="Pronto       ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()
import ply.lex as lex
import re

class myLexer(object):
	_instance = None

	def __new__(self, textOutput=None):
		if (self._instance is None):
			self._instance = super().__new__(self)
		return self._instance

	def __init__(self, textOutput=None):
		self.textOutput = textOutput
		self.input = ""
		self.output = ""
		self.lexer = None

		self.tokensExtenso = {
		'REAL': 'TIPO REAL',					
		'INT': 'TIPO INTEIRO', 						
		'BOOLEAN': 'TIPO BOOLEANO',						
		'NUM_REAL': 'NUMERO REAL',
		'NUM_INT': 'NUMERO INTEIRO',
		'OPSOMA': 'OPERADOR SOMA',			
		'OPSUB': 'OPERADOR SUBTRACAO', 				
		'OPMUL': 'OPERADOR MULTIPLICACAO', 			
		'OPDIV': 'OPERADOR DIVISAO', 				
		'OPIGUAL_ATRIB': 'OPERADOR ATRIBUIÇÃO',		
		'IGUAL': 'OPERADOR COMPARAÇÃO',		
		'DESIGUAL': 'OPERADOR DIFERENTE',
		'MAIOR': 'OPERADOR MAIOR',
		'MENOR': 'OPERADOR MENOR',
		'MAIOR_IGUAL': 'OPERADOR MAIOR OU IGUAL',
		'MENOR_IGUAL': 'OPERADOR MENOR OU IGUAL',
		'AP': 'ABRE PARENTESES',    				
		'FP': 'FECHA PARENTESES',	 				
		'ID': 'IDENTIFICADOR', 						
		'PROGRAM': 'INICIO DO PROGRAMA',			
		'BEGIN': 'INICIO DO BLOCO',					
		'END': 'FIM DO BLOCO',						
		'PROCEDURE': 'DECLARANDO PROCEDIMENTO',		
		'VAR': 'DECLARANDO VARIAVEL', 
		'READ': 'COMANDO DE ENTRADA',
		'WRITE': 'COMANDO DE SAIDA', 
		'TRUE': 'VALOR BOOLEANO VERDADEIRO',
		'FALSE': 'VALOR BOOLEANO FALSE', 
		'IF': "COMANDO 'SE'",
		'THEN': "COMANDO 'ENTAO'",
		'ELSE': "COMANDO 'SE NAO'",
		'WHILE': "COMANDO 'ENQUANTO'",
		'DO': "COMANDO 'FAÇA'",
		'DIV': "FUNÇAO DIVISAO",
		'AND': "OPERADOR LÓGICO 'E'",
		'OR': "OPERADOR LÓGICO 'OU'",
		'NOT': "OPERADOR LÓGICO 'NAO'",
		'FIM_LINHA': 'FINAL DA LINHA',
		'SEPARADOR': "SEPARADOR VIRGULA",
		'PONTO_FINAL': 'PONTO FINAL',
		'DOIS_PONTOS': 'DOIS PONTOS',
		}

		#PALAVRAS-RESERVADAS
		self.reserved = {
			'program': 'PROGRAM',
			'begin': 'BEGIN',
			'end': 'END',
			'int': 'INT',
			'real': 'REAL',
			'boolean': 'BOOLEAN',
			'procedure': 'PROCEDURE',
			'var': 'VAR',
			'read': 'READ',
			'write': 'WRITE',
			'true': 'TRUE',
			'false': 'FALSE',
			'if': 'IF',
			'then': 'THEN',
			'else': 'ELSE',
			'while': 'WHILE',
			'do': 'DO',
			'div': 'DIV', 
			'and': 'AND',
			'or': 'OR',
			'not': 'NOT',
		}

		#PALAVRAS-RESERVADAS
		reserved = {
			'program': 'PROGRAM',
			'begin': 'BEGIN',
			'end': 'END',
			'int': 'INT',
			'real': 'REAL',
			'boolean': 'BOOLEAN',
			'procedure': 'PROCEDURE',
			'var': 'VAR',
			'read': 'READ',
			'write': 'WRITE',
			'true': 'TRUE',
			'false': 'FALSE',
			'if': 'IF',
			'then': 'THEN',
			'else': 'ELSE',
			'while': 'WHILE',
			'do': 'DO',
			'div': 'DIV',
			'and': 'AND',
			'or': 'OR',
			'not': 'NOT',
		}

	# DEFININDO PARAMETROS DO ANALISADOR LEXICO
	tokens = [
		'NUM_REAL',					
		'NUM_INT', 				
		'OPSUB', 				
		'OPDIV', 				
		'OPIGUAL_ATRIB',		
		'IGUAL',				
		'DESIGUAL',
		'MAIOR',
		'MENOR',
		'MAIOR_IGUAL',
		'MENOR_IGUAL',
		'FIM_LINHA',			
		'SEPARADOR', 		
		'PONTO_FINAL', 			
		'DOIS_PONTOS',			
		'AP',    				
		'FP',	 				
		'ID',               	
	] + list(reserved.values())

	#DEFINIÇÃO DAS OPERAÇÕES
	t_OPSOMA = r'\+'
	t_OPSUB = r'-'
	t_OPMUL = r'\*'
	t_OPDIV = r'/'
	t_AP = r'[(]'
	t_FP = r'[)]'

	t_OPIGUAL_ATRIB = r':='
	t_DOIS_PONTOS = r':'
	t_IGUAL = r'='
	t_DESIGUAL = r'<>'
	t_MAIOR_IGUAL = r'>='
	t_MAIOR = r'>'
	t_MENOR_IGUAL = r'<='
	t_MENOR = r'<'

	t_FIM_LINHA = r';'
	t_SEPARADOR = r','
	t_PONTO_FINAL = r'[.]'

	# CARACTERES IGNORADOS
	t_ignore = ' \t'

	def getTokens(self):
		return self.tokens

	# NUMEROS E IDENTIFICADORES
	def t_ID(self, t):
		r'[a-zA-Z_][a-zA-Z_0-9]{0,50}' #LIMITE DE CARACTERES
		t.type = self.reserved.get(t.value,'ID')   #CHECAGEM DE PALAVRAS RESERVADAS
		return t

	# Especificação em forma de função, pois no caso dos numeros é necessária uma conversão deles
	def t_NUM_REAL(self, t):
		r'[+-]?(\d+\.\d+)'
		t.value = float(t.value)
		return t

	def t_NUM_INT(self, t):
		r'\d{1,40}' #1 ATÉ 40 DIGÍTOS
		try:
			t.value = int(t.value)
		except:
			print("Valor do inteiro muito grande: ", t.value)
			t.value = 0
		return t

	# CONTAGEM DE LINHAS E COLUNAS
	def t_newline(self, t):
		r'\n+'
		t.lexer.lineno += len(t.value)
		self.output = self.output + "\nLINHA %d: \n" % t.lexer.lineno
		
	def find_column(self, token):
		line_start = self.input.rfind('\n', 0, token.lexpos) + 1
		return (token.lexpos - line_start) + 1

	# COMENTÁRIOS
	def t_COMMENT(self, t):
		r'//.*|{[\s\S]*}'
		pass

	# LIDANDO COM ERROS
	def t_error(self, t):
		if(t.value != '{'):
			self.output = self.output + "Caracter invalido '%s'" % t.value[0] + " - Linha %d " % t.lineno + " - Coluna %d \n" % self.find_column(t)
		
		elif(t.value == '{'):
			self.output = self.output + "Comentario iniciado e não finalizado - Linha %d " % t.lineno + " - Coluna %d \n" % self.find_column(t)
		
		if(self.textOutput != None):
			self.textOutput.setText(self.output)
		t.lexer.skip(1)

	#CRIANDO ANALISADOR LÉXICO
	def build(self, **kwargs):
		if(self.lexer == None):
			self.lexer = lex.lex(module=self, **kwargs, debug=False)
		return self.lexer

	#USANDO ANALISADOR
	def use(self, text):
		self.output = "LINHA 1: \n"
		self.input = text
		self.lexer.input(text)
		for token in self.lexer:
			if not token:
				break
			self.output = self.output + str(token.value) + " => " + str(self.tokensExtenso[token.type]) +"\n"

		if(self.textOutput != None):
			self.textOutput.setText(self.output)
		self.output = ""


# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPSOMAOPSUBleftOPMULOPDIVleftIFleftELSEleftBEGINleftINTREALBOOLEANAND AP BEGIN BOOLEAN DESIGUAL DIV DO DOIS_PONTOS ELSE END FALSE FIM_LINHA FP ID IF IGUAL INT MAIOR MAIOR_IGUAL MENOR MENOR_IGUAL NOT NUM_INT NUM_REAL OPDIV OPIGUAL_ATRIB OPMUL OPSOMA OPSUB OR PONTO_FINAL PROCEDURE PROGRAM READ REAL SEPARADOR THEN TRUE VAR WHILE WRITEprograma :  PROGRAM ID FIM_LINHA bloco comando_composto PONTO_FINAL fim_programa\n        fim_programa : \n\n        bloco : new_scope parte_declaracao_de_variaveis parte_declaracao_de_subrotinas\n        parte_declaracao_de_variaveis :  declaracao_de_variaveis FIM_LINHA parte_declaracao_de_variaveis\n                                          | empty\n        declaracao_de_variaveis : tipo_simples lista_de_parametros\n        tipo_simples : INT\n                        | REAL\n                        | BOOLEAN\n        parte_declaracao_de_subrotinas : declaracao_de_procedimento\n                                          | empty\n        declaracao_de_procedimento : PROCEDURE ID parametros_formais FIM_LINHA bloco comando_composto FIM_LINHA\n        parametros_formais : AP mais_parametros_formais FP\n    \n        mais_parametros_formais : FIM_LINHA lista_de_parametros DOIS_PONTOS tipo_simples mais_parametros_formais\n                                    | lista_de_parametros DOIS_PONTOS tipo_simples mais_parametros_formais\n                                    | empty\n    \n        comando_composto : BEGIN new_begin comandos END\n                            \n        new_scope :new_begin :warnings : comandos : atribuicao FIM_LINHA comandos\n                    | chamada_de_procedimento FIM_LINHA comandos\n                    | comando_composto comandos\n                    | comando_condicional_1 comandos\n                    | comando_repetitivo_1 comandos\n                    | empty\n        atribuicao : variavel OPIGUAL_ATRIB expressao \n        comando_condicional_1 : IF  AP expressao FP THEN verifica_IF comandos desvio_IF %prec IF \n                                 | IF  AP expressao FP THEN verifica_IF comandos desvio_IF ELSE verifica_ELSE comandos desvio_ELSE %prec ELSE\n         verifica_IF :\n         desvio_IF :\n         verifica_ELSE :\n         desvio_ELSE :\n        comando_repetitivo_1 : WHILE AP set_expressao expressao verifica_WHILE FP DO comando_composto desvio_WHILE\n        set_expressao :   verifica_WHILE :\n         desvio_WHILE :\n        chamada_de_procedimento : variavel AP lista_de_parametros FP\n                                   | READ AP lista_de_parametros FP\n                                   | WRITE AP lista_de_parametros FP\n        lista_de_parametros : expressao mais_parametros\n                               | empty\n        mais_parametros : SEPARADOR lista_de_parametros\n                            | empty\n        expressao : expressao_simples      \n                     | expressao_simples relacao expressao_simples\n        relacao : IGUAL   \n                   | MAIOR_IGUAL\n                   | MAIOR\n                   | MENOR_IGUAL\n                   | MENOR expressao_simples : expressao_simples OPSOMA termo\n                             | expressao_simples OPSUB termo\n                             | expressao_simples OR termo\n                             | termo \n                \n         termo : termo OPMUL fator\n                 | termo OPDIV fator\n                 | termo DIV fator\n                 | termo AND fator\n                 | fator\n         fator : numero  \n                 | variavel \n                 | TRUE\n                 | FALSE\n                 | AP expressao_simples FP\n                 | NOT fator\n        numero : NUM_INT\n                  | NUM_REAL \n                              \n        variavel : ID     \n        empty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,16,38,],[0,-2,-1,]),'ID':([2,8,12,13,14,15,17,21,33,34,42,43,44,45,54,56,57,58,59,60,61,62,63,64,65,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,84,95,96,102,105,117,121,122,125,127,130,131,132,133,134,135,136,],[3,-19,37,-7,-8,-9,37,51,37,37,37,37,37,-26,37,37,37,37,37,-47,-48,-49,-50,-51,37,37,37,37,-17,37,37,-23,-24,-25,37,37,37,37,37,-35,37,-21,-22,37,37,-30,37,37,37,-31,-28,-37,-32,-34,37,-33,-29,]),'FIM_LINHA':([3,10,12,13,14,15,23,24,25,26,27,28,29,30,31,32,35,36,37,40,41,53,54,55,70,71,83,84,85,86,87,88,89,90,91,92,93,94,97,108,109,110,114,119,121,125,],[4,22,-70,-7,-8,-9,-6,-70,-42,-45,-55,-60,-61,-62,-63,-64,-67,-68,-69,72,73,-41,-70,-44,-66,-17,103,105,-43,-46,-52,-53,-54,-56,-57,-58,-59,-65,-27,-38,-39,-40,-13,124,105,105,]),'INT':([4,6,22,103,116,120,],[-18,13,13,-18,13,13,]),'REAL':([4,6,22,103,116,120,],[-18,14,14,-18,14,14,]),'BOOLEAN':([4,6,22,103,116,120,],[-18,15,15,-18,15,15,]),'PROCEDURE':([4,6,9,11,22,52,103,],[-18,-70,21,-5,-70,-4,-18,]),'BEGIN':([4,5,6,8,9,11,17,18,19,20,22,42,43,44,45,52,71,72,73,74,75,76,95,96,103,113,117,122,124,127,128,130,131,132,133,134,135,136,],[-18,8,-70,-19,-70,-5,8,-3,-10,-11,-70,8,8,8,-26,-4,-17,8,8,-23,-24,-25,-21,-22,-18,8,-30,8,-12,-31,8,-28,-37,-32,-34,8,-33,-29,]),'PONTO_FINAL':([7,71,],[16,-17,]),'READ':([8,17,42,43,44,45,71,72,73,74,75,76,95,96,117,122,127,130,131,132,133,134,135,136,],[-19,47,47,47,47,-26,-17,47,47,-23,-24,-25,-21,-22,-30,47,-31,-28,-37,-32,-34,47,-33,-29,]),'WRITE':([8,17,42,43,44,45,71,72,73,74,75,76,95,96,117,122,127,130,131,132,133,134,135,136,],[-19,48,48,48,48,-26,-17,48,48,-23,-24,-25,-21,-22,-30,48,-31,-28,-37,-32,-34,48,-33,-29,]),'IF':([8,17,42,43,44,45,71,72,73,74,75,76,95,96,117,122,127,130,131,132,133,134,135,136,],[-19,49,49,49,49,-26,-17,49,49,-23,-24,-25,-21,-22,-30,49,-31,-28,-37,-32,-34,49,-33,-29,]),'WHILE':([8,17,42,43,44,45,71,72,73,74,75,76,95,96,117,122,127,130,131,132,133,134,135,136,],[-19,50,50,50,50,-26,-17,50,50,-23,-24,-25,-21,-22,-30,50,-31,-28,-37,-32,-34,50,-33,-29,]),'END':([8,17,39,42,43,44,45,71,72,73,74,75,76,95,96,117,122,127,130,131,132,133,134,135,136,],[-19,-70,71,-70,-70,-70,-26,-17,-70,-70,-23,-24,-25,-21,-22,-30,-70,-31,-28,-37,-32,-34,-70,-33,-29,]),'TRUE':([12,13,14,15,33,34,54,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,84,102,105,121,125,],[31,-7,-8,-9,31,31,31,31,31,31,31,-47,-48,-49,-50,-51,31,31,31,31,31,31,31,31,31,-35,31,31,31,31,31,]),'FALSE':([12,13,14,15,33,34,54,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,84,102,105,121,125,],[32,-7,-8,-9,32,32,32,32,32,32,32,-47,-48,-49,-50,-51,32,32,32,32,32,32,32,32,32,-35,32,32,32,32,32,]),'AP':([12,13,14,15,33,34,37,46,47,48,49,50,51,54,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,84,102,105,121,125,],[33,-7,-8,-9,33,33,-69,78,79,80,81,82,84,33,33,33,33,33,-47,-48,-49,-50,-51,33,33,33,33,33,33,33,33,33,-35,33,33,33,33,33,]),'NOT':([12,13,14,15,33,34,54,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,84,102,105,121,125,],[34,-7,-8,-9,34,34,34,34,34,34,34,-47,-48,-49,-50,-51,34,34,34,34,34,34,34,34,34,-35,34,34,34,34,34,]),'NUM_INT':([12,13,14,15,33,34,54,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,84,102,105,121,125,],[35,-7,-8,-9,35,35,35,35,35,35,35,-47,-48,-49,-50,-51,35,35,35,35,35,35,35,35,35,-35,35,35,35,35,35,]),'NUM_REAL':([12,13,14,15,33,34,54,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,81,82,84,102,105,121,125,],[36,-7,-8,-9,36,36,36,36,36,36,36,-47,-48,-49,-50,-51,36,36,36,36,36,36,36,36,36,-35,36,36,36,36,36,]),'DOIS_PONTOS':([13,14,15,24,25,26,27,28,29,30,31,32,35,36,37,53,54,55,70,84,85,86,87,88,89,90,91,92,93,94,105,106,107,115,121,125,],[-7,-8,-9,-70,-42,-45,-55,-60,-61,-62,-63,-64,-67,-68,-69,-41,-70,-44,-66,-70,-43,-46,-52,-53,-54,-56,-57,-58,-59,-65,-70,116,-42,120,-70,-70,]),'FP':([13,14,15,24,25,26,27,28,29,30,31,32,35,36,37,53,54,55,69,70,78,79,80,84,85,86,87,88,89,90,91,92,93,94,98,99,100,101,104,107,112,118,121,125,126,129,],[-7,-8,-9,-70,-42,-45,-55,-60,-61,-62,-63,-64,-67,-68,-69,-41,-70,-44,94,-66,-70,-70,-70,-70,-43,-46,-52,-53,-54,-56,-57,-58,-59,-65,108,109,110,111,114,-16,-36,123,-70,-70,-15,-14,]),'SEPARADOR':([24,26,27,28,29,30,31,32,35,36,37,70,86,87,88,89,90,91,92,93,94,],[54,-45,-55,-60,-61,-62,-63,-64,-67,-68,-69,-66,-46,-52,-53,-54,-56,-57,-58,-59,-65,]),'OPSOMA':([26,27,28,29,30,31,32,35,36,37,69,70,86,87,88,89,90,91,92,93,94,],[57,-55,-60,-61,-62,-63,-64,-67,-68,-69,57,-66,57,-52,-53,-54,-56,-57,-58,-59,-65,]),'OPSUB':([26,27,28,29,30,31,32,35,36,37,69,70,86,87,88,89,90,91,92,93,94,],[58,-55,-60,-61,-62,-63,-64,-67,-68,-69,58,-66,58,-52,-53,-54,-56,-57,-58,-59,-65,]),'OR':([26,27,28,29,30,31,32,35,36,37,69,70,86,87,88,89,90,91,92,93,94,],[59,-55,-60,-61,-62,-63,-64,-67,-68,-69,59,-66,59,-52,-53,-54,-56,-57,-58,-59,-65,]),'IGUAL':([26,27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[60,-55,-60,-61,-62,-63,-64,-67,-68,-69,-66,-52,-53,-54,-56,-57,-58,-59,-65,]),'MAIOR_IGUAL':([26,27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[61,-55,-60,-61,-62,-63,-64,-67,-68,-69,-66,-52,-53,-54,-56,-57,-58,-59,-65,]),'MAIOR':([26,27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[62,-55,-60,-61,-62,-63,-64,-67,-68,-69,-66,-52,-53,-54,-56,-57,-58,-59,-65,]),'MENOR_IGUAL':([26,27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[63,-55,-60,-61,-62,-63,-64,-67,-68,-69,-66,-52,-53,-54,-56,-57,-58,-59,-65,]),'MENOR':([26,27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[64,-55,-60,-61,-62,-63,-64,-67,-68,-69,-66,-52,-53,-54,-56,-57,-58,-59,-65,]),'OPMUL':([27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[65,-60,-61,-62,-63,-64,-67,-68,-69,-66,65,65,65,-56,-57,-58,-59,-65,]),'OPDIV':([27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[66,-60,-61,-62,-63,-64,-67,-68,-69,-66,66,66,66,-56,-57,-58,-59,-65,]),'DIV':([27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[67,-60,-61,-62,-63,-64,-67,-68,-69,-66,67,67,67,-56,-57,-58,-59,-65,]),'AND':([27,28,29,30,31,32,35,36,37,70,87,88,89,90,91,92,93,94,],[68,-60,-61,-62,-63,-64,-67,-68,-69,-66,68,68,68,-56,-57,-58,-59,-65,]),'OPIGUAL_ATRIB':([37,46,],[-69,77,]),'ELSE':([42,43,44,45,71,72,73,74,75,76,95,96,117,122,127,130,131,132,133,134,135,136,],[-70,-70,-70,-26,-17,-70,-70,-23,-24,-25,-21,-22,-30,-70,-31,132,-37,-32,-34,-70,-33,-29,]),'THEN':([111,],[117,]),'DO':([123,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloco':([4,103,],[5,113,]),'new_scope':([4,103,],[6,6,]),'comando_composto':([5,17,42,43,44,72,73,113,122,128,134,],[7,42,42,42,42,42,42,119,42,131,42,]),'parte_declaracao_de_variaveis':([6,22,],[9,52,]),'declaracao_de_variaveis':([6,22,],[10,10,]),'empty':([6,9,12,17,22,24,42,43,44,54,72,73,78,79,80,84,105,121,122,125,134,],[11,20,25,45,11,55,45,45,45,25,45,45,25,25,25,107,25,107,45,107,45,]),'tipo_simples':([6,22,116,120,],[12,12,121,125,]),'new_begin':([8,],[17,]),'parte_declaracao_de_subrotinas':([9,],[18,]),'declaracao_de_procedimento':([9,],[19,]),'lista_de_parametros':([12,54,78,79,80,84,105,121,125,],[23,85,98,99,100,106,115,106,106,]),'expressao':([12,54,77,78,79,80,81,84,102,105,121,125,],[24,24,97,24,24,24,101,24,112,24,24,24,]),'expressao_simples':([12,33,54,56,77,78,79,80,81,84,102,105,121,125,],[26,69,26,86,26,26,26,26,26,26,26,26,26,26,]),'termo':([12,33,54,56,57,58,59,77,78,79,80,81,84,102,105,121,125,],[27,27,27,27,87,88,89,27,27,27,27,27,27,27,27,27,27,]),'fator':([12,33,34,54,56,57,58,59,65,66,67,68,77,78,79,80,81,84,102,105,121,125,],[28,28,70,28,28,28,28,28,90,91,92,93,28,28,28,28,28,28,28,28,28,28,]),'numero':([12,33,34,54,56,57,58,59,65,66,67,68,77,78,79,80,81,84,102,105,121,125,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'variavel':([12,17,33,34,42,43,44,54,56,57,58,59,65,66,67,68,72,73,77,78,79,80,81,84,102,105,121,122,125,134,],[30,46,30,30,46,46,46,30,30,30,30,30,30,30,30,30,46,46,30,30,30,30,30,30,30,30,30,46,30,46,]),'fim_programa':([16,],[38,]),'comandos':([17,42,43,44,72,73,122,134,],[39,74,75,76,95,96,127,135,]),'atribuicao':([17,42,43,44,72,73,122,134,],[40,40,40,40,40,40,40,40,]),'chamada_de_procedimento':([17,42,43,44,72,73,122,134,],[41,41,41,41,41,41,41,41,]),'comando_condicional_1':([17,42,43,44,72,73,122,134,],[43,43,43,43,43,43,43,43,]),'comando_repetitivo_1':([17,42,43,44,72,73,122,134,],[44,44,44,44,44,44,44,44,]),'mais_parametros':([24,],[53,]),'relacao':([26,],[56,]),'parametros_formais':([51,],[83,]),'set_expressao':([82,],[102,]),'mais_parametros_formais':([84,121,125,],[104,126,129,]),'verifica_WHILE':([112,],[118,]),'verifica_IF':([117,],[122,]),'desvio_IF':([127,],[130,]),'desvio_WHILE':([131,],[133,]),'verifica_ELSE':([132,],[134,]),'desvio_ELSE':([135,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID FIM_LINHA bloco comando_composto PONTO_FINAL fim_programa','programa',7,'p_programa','parser.py',67),
  ('fim_programa -> <empty>','fim_programa',0,'p_fim_programa','parser.py',80),
  ('bloco -> new_scope parte_declaracao_de_variaveis parte_declaracao_de_subrotinas','bloco',3,'p_bloco','parser.py',85),
  ('parte_declaracao_de_variaveis -> declaracao_de_variaveis FIM_LINHA parte_declaracao_de_variaveis','parte_declaracao_de_variaveis',3,'p_parte_declaracao_de_variaveis','parser.py',94),
  ('parte_declaracao_de_variaveis -> empty','parte_declaracao_de_variaveis',1,'p_parte_declaracao_de_variaveis','parser.py',95),
  ('declaracao_de_variaveis -> tipo_simples lista_de_parametros','declaracao_de_variaveis',2,'p_declaracao_de_variaveis','parser.py',111),
  ('tipo_simples -> INT','tipo_simples',1,'p_tipo_simples','parser.py',130),
  ('tipo_simples -> REAL','tipo_simples',1,'p_tipo_simples','parser.py',131),
  ('tipo_simples -> BOOLEAN','tipo_simples',1,'p_tipo_simples','parser.py',132),
  ('parte_declaracao_de_subrotinas -> declaracao_de_procedimento','parte_declaracao_de_subrotinas',1,'p_parte_declaracao_de_subrotinas','parser.py',138),
  ('parte_declaracao_de_subrotinas -> empty','parte_declaracao_de_subrotinas',1,'p_parte_declaracao_de_subrotinas','parser.py',139),
  ('declaracao_de_procedimento -> PROCEDURE ID parametros_formais FIM_LINHA bloco comando_composto FIM_LINHA','declaracao_de_procedimento',7,'p_declaracao_de_procedimento','parser.py',150),
  ('parametros_formais -> AP mais_parametros_formais FP','parametros_formais',3,'p_parametros_formais','parser.py',166),
  ('mais_parametros_formais -> FIM_LINHA lista_de_parametros DOIS_PONTOS tipo_simples mais_parametros_formais','mais_parametros_formais',5,'p_mais_parametros_formais','parser.py',174),
  ('mais_parametros_formais -> lista_de_parametros DOIS_PONTOS tipo_simples mais_parametros_formais','mais_parametros_formais',4,'p_mais_parametros_formais','parser.py',175),
  ('mais_parametros_formais -> empty','mais_parametros_formais',1,'p_mais_parametros_formais','parser.py',176),
  ('comando_composto -> BEGIN new_begin comandos END','comando_composto',4,'p_comando_composto','parser.py',195),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','parser.py',208),
  ('new_begin -> <empty>','new_begin',0,'p_new_begin','parser.py',214),
  ('warnings -> <empty>','warnings',0,'p_warnings','parser.py',221),
  ('comandos -> atribuicao FIM_LINHA comandos','comandos',3,'p_comandos','parser.py',231),
  ('comandos -> chamada_de_procedimento FIM_LINHA comandos','comandos',3,'p_comandos','parser.py',232),
  ('comandos -> comando_composto comandos','comandos',2,'p_comandos','parser.py',233),
  ('comandos -> comando_condicional_1 comandos','comandos',2,'p_comandos','parser.py',234),
  ('comandos -> comando_repetitivo_1 comandos','comandos',2,'p_comandos','parser.py',235),
  ('comandos -> empty','comandos',1,'p_comandos','parser.py',236),
  ('atribuicao -> variavel OPIGUAL_ATRIB expressao','atribuicao',3,'p_atribuicao','parser.py',247),
  ('comando_condicional_1 -> IF AP expressao FP THEN verifica_IF comandos desvio_IF','comando_condicional_1',8,'p_comando_condicional_1','parser.py',277),
  ('comando_condicional_1 -> IF AP expressao FP THEN verifica_IF comandos desvio_IF ELSE verifica_ELSE comandos desvio_ELSE','comando_condicional_1',12,'p_comando_condicional_1','parser.py',278),
  ('verifica_IF -> <empty>','verifica_IF',0,'p_verifica_IF','parser.py',296),
  ('desvio_IF -> <empty>','desvio_IF',0,'p_desvio_IF','parser.py',301),
  ('verifica_ELSE -> <empty>','verifica_ELSE',0,'p_verifica_ELSE','parser.py',306),
  ('desvio_ELSE -> <empty>','desvio_ELSE',0,'p_desvio_ELSE','parser.py',312),
  ('comando_repetitivo_1 -> WHILE AP set_expressao expressao verifica_WHILE FP DO comando_composto desvio_WHILE','comando_repetitivo_1',9,'p_comando_repetitivo_1','parser.py',320),
  ('set_expressao -> <empty>','set_expressao',0,'p_set_expressao','parser.py',330),
  ('verifica_WHILE -> <empty>','verifica_WHILE',0,'p_verifica_WHILE','parser.py',335),
  ('desvio_WHILE -> <empty>','desvio_WHILE',0,'p_desvio_WHILE','parser.py',340),
  ('chamada_de_procedimento -> variavel AP lista_de_parametros FP','chamada_de_procedimento',4,'p_chamada_de_procedimento','parser.py',349),
  ('chamada_de_procedimento -> READ AP lista_de_parametros FP','chamada_de_procedimento',4,'p_chamada_de_procedimento','parser.py',350),
  ('chamada_de_procedimento -> WRITE AP lista_de_parametros FP','chamada_de_procedimento',4,'p_chamada_de_procedimento','parser.py',351),
  ('lista_de_parametros -> expressao mais_parametros','lista_de_parametros',2,'p_lista_de_parametros','parser.py',415),
  ('lista_de_parametros -> empty','lista_de_parametros',1,'p_lista_de_parametros','parser.py',416),
  ('mais_parametros -> SEPARADOR lista_de_parametros','mais_parametros',2,'p_mais_parametros','parser.py',435),
  ('mais_parametros -> empty','mais_parametros',1,'p_mais_parametros','parser.py',436),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','parser.py',444),
  ('expressao -> expressao_simples relacao expressao_simples','expressao',3,'p_expressao','parser.py',445),
  ('relacao -> IGUAL','relacao',1,'p_relacao','parser.py',534),
  ('relacao -> MAIOR_IGUAL','relacao',1,'p_relacao','parser.py',535),
  ('relacao -> MAIOR','relacao',1,'p_relacao','parser.py',536),
  ('relacao -> MENOR_IGUAL','relacao',1,'p_relacao','parser.py',537),
  ('relacao -> MENOR','relacao',1,'p_relacao','parser.py',538),
  ('expressao_simples -> expressao_simples OPSOMA termo','expressao_simples',3,'p_expressao_simples','parser.py',545),
  ('expressao_simples -> expressao_simples OPSUB termo','expressao_simples',3,'p_expressao_simples','parser.py',546),
  ('expressao_simples -> expressao_simples OR termo','expressao_simples',3,'p_expressao_simples','parser.py',547),
  ('expressao_simples -> termo','expressao_simples',1,'p_expressao_simples','parser.py',548),
  ('termo -> termo OPMUL fator','termo',3,'p_termo','parser.py',606),
  ('termo -> termo OPDIV fator','termo',3,'p_termo','parser.py',607),
  ('termo -> termo DIV fator','termo',3,'p_termo','parser.py',608),
  ('termo -> termo AND fator','termo',3,'p_termo','parser.py',609),
  ('termo -> fator','termo',1,'p_termo','parser.py',610),
  ('fator -> numero','fator',1,'p_fator','parser.py',681),
  ('fator -> variavel','fator',1,'p_fator','parser.py',682),
  ('fator -> TRUE','fator',1,'p_fator','parser.py',683),
  ('fator -> FALSE','fator',1,'p_fator','parser.py',684),
  ('fator -> AP expressao_simples FP','fator',3,'p_fator','parser.py',685),
  ('fator -> NOT fator','fator',2,'p_fator','parser.py',686),
  ('numero -> NUM_INT','numero',1,'p_numero','parser.py',711),
  ('numero -> NUM_REAL','numero',1,'p_numero','parser.py',712),
  ('variavel -> ID','variavel',1,'p_variavel','parser.py',719),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',726),
]

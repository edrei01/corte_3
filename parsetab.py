
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AGUSTICIDAD ASSIGN COMILLA CONTENIDO DESIGUAL DIV DOBLEIGUAL DOUBLESTRING ENTERO GREATER ID ID IGUALMA IGUALMENO INCREMENT LBRACE LPAREN MAS MENOR MENOS MULTI NOVASIR NUMBER PAN PARAQOQUE PUNTCOM RBRACE RPAREN SEMI SIONO STRING UBUBUE VASIR VUELAOQUEinit : program\n                | opcion2\n                | opcion3\n                | opcion4\n                | ububuefunopcion2 : AGUSTICIDAD UBUBUE ID ASSIGN ID\n                    | AGUSTICIDAD PAN ID ASSIGN NUMBERvar : AGUSTICIDAD PAN ID ASSIGN NUMBERopcion3 : opcion2 VASIR LPAREN ID operador ident RPAREN LBRACE cualquierIF RBRACE NOVASIR LBRACE cualquierELSE RBRACEopcion4 : VUELAOQUE ID LPAREN PAN ID RPAREN LBRACE opcion2 var ID ASSIGN ID MAS ID RBRACEububuefun : VUELAOQUE ID LPAREN UBUBUE ID RPAREN LBRACE ID ASSIGN ID RBRACEprogram : PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE cualquier RBRACEvariable : UBUBUE\n                    | PANcualquier : CONTENIDO\n                     | IDcualquierIF : CONTENIDO\n                     | IDcualquierELSE : CONTENIDO\n                     | IDoperador : GREATER\n                    | IGUALMA\n                    | IGUALMENO\n                    | DOBLEIGUAL\n                    | MENOR\n                    | DESIGUAL\n                    | ASSIGNident : ID  \n                 | NUMBER'
    
_lr_action_items = {'PARAQOQUE':([0,],[7,]),'AGUSTICIDAD':([0,37,38,49,53,],[8,-6,-7,8,60,]),'VUELAOQUE':([0,],[9,]),'$end':([1,2,3,4,5,6,37,38,71,82,86,91,],[0,-1,-2,-3,-4,-5,-6,-7,-11,-9,-10,-12,]),'VASIR':([3,37,38,],[10,-6,-7,]),'LPAREN':([7,10,14,],[11,15,21,]),'UBUBUE':([8,11,21,],[12,17,27,]),'PAN':([8,11,21,60,],[13,18,26,65,]),'ID':([9,12,13,15,16,17,18,24,26,27,28,29,30,31,32,33,34,35,48,50,51,59,61,65,68,69,72,80,81,87,],[14,19,20,22,23,-13,-14,37,39,40,41,-21,-22,-23,-24,-25,-26,-27,52,54,55,64,66,70,73,74,76,84,-8,88,]),'ASSIGN':([19,20,22,23,52,54,64,70,],[24,25,35,36,35,61,69,75,]),'GREATER':([22,52,],[29,29,]),'IGUALMA':([22,52,],[30,30,]),'IGUALMENO':([22,52,],[31,31,]),'DOBLEIGUAL':([22,52,],[32,32,]),'MENOR':([22,52,],[33,33,]),'DESIGUAL':([22,52,],[34,34,]),'NUMBER':([25,28,29,30,31,32,33,34,35,36,58,75,],[38,43,-21,-22,-23,-24,-25,-26,-27,44,63,81,]),'RPAREN':([39,40,41,42,43,83,],[45,46,-28,47,-29,85,]),'PUNTCOM':([44,63,79,],[48,68,83,]),'LBRACE':([45,46,47,67,85,],[49,50,51,72,87,]),'CONTENIDO':([51,72,87,],[57,78,90,]),'RBRACE':([55,56,57,66,76,77,78,84,88,89,90,],[-18,62,-17,71,-20,82,-19,86,-16,91,-15,]),'NOVASIR':([62,],[67,]),'INCREMENT':([73,],[79,]),'MAS':([74,],[80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'program':([0,],[2,]),'opcion2':([0,49,],[3,53,]),'opcion3':([0,],[4,]),'opcion4':([0,],[5,]),'ububuefun':([0,],[6,]),'variable':([11,],[16,]),'operador':([22,52,],[28,58,]),'ident':([28,],[42,]),'cualquierIF':([51,],[56,]),'var':([53,],[59,]),'cualquierELSE':([72,],[77,]),'cualquier':([87,],[89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> program','init',1,'p_init','semantico.py',12),
  ('init -> opcion2','init',1,'p_init','semantico.py',13),
  ('init -> opcion3','init',1,'p_init','semantico.py',14),
  ('init -> opcion4','init',1,'p_init','semantico.py',15),
  ('init -> ububuefun','init',1,'p_init','semantico.py',16),
  ('opcion2 -> AGUSTICIDAD UBUBUE ID ASSIGN ID','opcion2',5,'p_opcion2','semantico.py',19),
  ('opcion2 -> AGUSTICIDAD PAN ID ASSIGN NUMBER','opcion2',5,'p_opcion2','semantico.py',20),
  ('var -> AGUSTICIDAD PAN ID ASSIGN NUMBER','var',5,'p_var','semantico.py',35),
  ('opcion3 -> opcion2 VASIR LPAREN ID operador ident RPAREN LBRACE cualquierIF RBRACE NOVASIR LBRACE cualquierELSE RBRACE','opcion3',14,'p_opcion3','semantico.py',44),
  ('opcion4 -> VUELAOQUE ID LPAREN PAN ID RPAREN LBRACE opcion2 var ID ASSIGN ID MAS ID RBRACE','opcion4',15,'p_opcion4','semantico.py',89),
  ('ububuefun -> VUELAOQUE ID LPAREN UBUBUE ID RPAREN LBRACE ID ASSIGN ID RBRACE','ububuefun',11,'p_ububuefun','semantico.py',108),
  ('program -> PARAQOQUE LPAREN variable ID ASSIGN NUMBER PUNTCOM ID operador NUMBER PUNTCOM ID INCREMENT PUNTCOM RPAREN LBRACE cualquier RBRACE','program',18,'p_program','semantico.py',115),
  ('variable -> UBUBUE','variable',1,'p_variable','semantico.py',132),
  ('variable -> PAN','variable',1,'p_variable','semantico.py',133),
  ('cualquier -> CONTENIDO','cualquier',1,'p_cualquier','semantico.py',138),
  ('cualquier -> ID','cualquier',1,'p_cualquier','semantico.py',139),
  ('cualquierIF -> CONTENIDO','cualquierIF',1,'p_cualquierIF','semantico.py',143),
  ('cualquierIF -> ID','cualquierIF',1,'p_cualquierIF','semantico.py',144),
  ('cualquierELSE -> CONTENIDO','cualquierELSE',1,'p_cualquierELSE','semantico.py',149),
  ('cualquierELSE -> ID','cualquierELSE',1,'p_cualquierELSE','semantico.py',150),
  ('operador -> GREATER','operador',1,'p_operador','semantico.py',155),
  ('operador -> IGUALMA','operador',1,'p_operador','semantico.py',156),
  ('operador -> IGUALMENO','operador',1,'p_operador','semantico.py',157),
  ('operador -> DOBLEIGUAL','operador',1,'p_operador','semantico.py',158),
  ('operador -> MENOR','operador',1,'p_operador','semantico.py',159),
  ('operador -> DESIGUAL','operador',1,'p_operador','semantico.py',160),
  ('operador -> ASSIGN','operador',1,'p_operador','semantico.py',161),
  ('ident -> ID','ident',1,'p_ident','semantico.py',166),
  ('ident -> NUMBER','ident',1,'p_ident','semantico.py',167),
]

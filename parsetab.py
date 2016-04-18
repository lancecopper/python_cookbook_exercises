
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '550F561BBF280D3D500E9EAFB89D936E'
    
_lr_action_items = {'RPAREN':([2,3,4,6,11,12,13,14,15,],[-7,-3,-6,11,-8,-5,-4,-1,-2,]),'DIVIDE':([2,3,4,11,12,13,14,15,],[-7,7,-6,-8,-5,-4,7,7,]),'NUM':([0,1,7,8,9,10,],[2,2,2,2,2,2,]),'MINUS':([2,3,4,5,6,11,12,13,14,15,],[-7,-3,-6,10,10,-8,-5,-4,-1,-2,]),'LPAREN':([0,1,7,8,9,10,],[1,1,1,1,1,1,]),'TIMES':([2,3,4,11,12,13,14,15,],[-7,8,-6,-8,-5,-4,8,8,]),'PLUS':([2,3,4,5,6,11,12,13,14,15,],[-7,-3,-6,9,9,-8,-5,-4,-1,-2,]),'$end':([2,3,4,5,11,12,13,14,15,],[-7,-3,-6,0,-8,-5,-4,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,1,9,10,],[3,3,14,15,]),'factor':([0,1,7,8,9,10,],[4,4,12,13,4,4,]),'expr':([0,1,],[5,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr PLUS term','expr',3,'p_expr','4.19.1.py',33),
  ('expr -> expr MINUS term','expr',3,'p_expr','4.19.1.py',34),
  ('expr -> term','expr',1,'p_expr_term','4.19.1.py',43),
  ('term -> term TIMES factor','term',3,'p_term','4.19.1.py',49),
  ('term -> term DIVIDE factor','term',3,'p_term','4.19.1.py',50),
  ('term -> factor','term',1,'p_term_factor','4.19.1.py',59),
  ('factor -> NUM','factor',1,'p_factor','4.19.1.py',65),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_group','4.19.1.py',71),
]

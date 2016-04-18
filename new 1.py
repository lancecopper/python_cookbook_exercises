from ply.lex import lex 						 
from ply.yacc import yacc 						 
# Token list 						 
tokens = [ 'NUM', 'PLUS', 'MINUS', 	'TIMES', 	'DIVIDE', 	'LPAREN', 	'RPAREN' 	] 	 
# Ignored characters 						 
t_ignore = ' \t\n' 						 
# Token specifications (as regexs) 						 
t_PLUS = r'\+' 						 
t_MINUS = r'-' 						 
t_TIMES = r'\*' 						 
t_DIVIDE = r'/' 						 
t_LPAREN = r'\(' 						 
t_RPAREN = r'\)' 						 
# Token processing functions 						 
def t_NUM(t): 						 
r'\d+' 						 
t.value = int(t.value) 						 

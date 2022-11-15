from analizadorLexico import analizador
from ply import yacc
def p_proc(p):
    '''S : proc ident parena P parenc'''
    pass

def p_P(p):
    '''P : params 
                | params coma P'''
    pass

def p_error(p):
  print("Error sintactico en la linea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')

parser = yacc.yacc() 
analizador.lineno = 0
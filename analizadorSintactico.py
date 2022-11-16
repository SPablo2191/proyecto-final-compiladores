from ply import yacc
from analizadorLexico import analizador,tokens

def p_start(p):
  """s : PROGINI programa PROGFIN"""

def p_programa(p):
  """programa : incluir programa
              | cuerpo"""

def p_cuerpo(p):
  """cuerpo :   pin cuerpo
              | definir cuerpo
              | asignar cuerpo
              | comLinea cuerpo
              | comBloque cuerpo
              | saltoLinea cuerpo
              | adelante cuerpo
              | atras cuerpo
              | izquierda cuerpo
              | derecha cuerpo
              | esperar cuerpo
              | parar cuerpo
              | if cuerpo
              | while cuerpo
              | funcion cuerpo
              | empty"""

def p_pin(p):
  """pin : DEF PIN inicioParentesis variable dosPuntos tipoPin finParentesis finLinea"""

def p_tipoPin(p):
  """tipoPin : SAL 
             | ENT"""

def p_incluir(p):
  """incluir : INCLUIR inicioParentesis comilla variable finLinea variable comilla finParentesis finLinea"""





def p_definir(p):
  """definir : DEFINIR inicioParentesis tipo variable asig valor finParentesis finLinea 
              | DEFINIR inicioParentesis tipo variable finParentesis finLinea 
              """

def p_tipo(p):
  """tipo : int 
          | float 
          | string 
          | bool"""

def p_valor(p):
  """valor : numero
            | comilla variable comilla
            | true
            | false"""

def p_asignar(p):
  """asignar : variable asig valor finLinea
              | variable asig variable finLinea"""

def p_finFuncion(p):
  """finFuncion : inicioParentesis finParentesis finLinea"""

def p_adelante(p):
  """adelante : ADEL finFuncion"""

def p_atras(p):
  """atras : ATR finFuncion"""

def p_izquierda(p):
  """izquierda : IZQ finFuncion"""

def p_derecha(p):
  """derecha : DER finFuncion"""

def p_parar(p):
  """parar : STOP finFuncion"""

def p_esperar(p):
  """esperar : ESP inicioParentesis numero finParentesis finLinea"""

def p_predicado(p):
  """predicado : false 
                | true 
                | valor operadorComp valor 
                | inicioParentesis predicado operadorLog predicado finParentesis
"""

def p_operadorLog(p):
  """operadorLog : AND
                  | OR"""

def p_if(p):
  """if : IF predicado BEGIN cuerpo END else"""

def p_else(p):
  """else : ELSE BEGIN cuerpo END
          | empty"""

def p_while(p):
  """while : WHILE predicado BEGIN cuerpo END"""

def p_funcion(p):
  """funcion : FUNC inicioParentesis parametros finParentesis retorno finLinea"""

def p_retorno(p):
  """retorno : dosPuntos tipo 
              | empty"""

def p_parametros(p):
  """parametros : tipo dosPuntos variable 
                | tipo dosPuntos variable coma parametros
                | empty"""

def p_empty(p):
  'empty :'
  pass
def p_error(p):
  print("Error sintactico en la linea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')

parser = yacc.yacc() 
analizador.lineno = 0
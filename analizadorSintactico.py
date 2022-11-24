from ply import yacc
from analizadorLexico import analizador,tokens
from callbacks import *
from traductor import traductorArduino
is_first_pin = False
is_first_reservadas = False

def p_start(p):
  """s : PROGINI programa PROGFIN"""
  pass

def p_programa(p):
  """programa : incluir programa
              | cuerpo"""
  pass

def p_cuerpo(p):
  """cuerpo :   pin cuerpo
              | definir cuerpo
              | asignar cuerpo
              | comLinea cuerpo
              | comBloque cuerpo
              | saltoLinea cuerpo
              | reservadas cuerpo
              | if cuerpo
              | while cuerpo
              | funcion cuerpo
              | empty"""
  pass

def p_pin(p):
  """pin : DEF PIN inicioParentesis variable dosPuntos pinTipo finParentesis finLinea"""
  is_first_pin = True if p_pin.counter <= 0 else False
  p_pin.counter += 1
  traductorArduino(p, cb_p_pin, is_first_pin=is_first_pin,is_pin=True)
  pass

p_pin.counter = 0



def p_pinTipo(p):
  """pinTipo : SAL 
             | ENT"""
  pass

def p_incluir(p):
  """incluir : INCLUIR inicioParentesis comilla variable finLinea variable comilla finParentesis finLinea"""
  traductorArduino(p,cb_p_incluir)
  pass




def p_definir(p):
  """definir  : DEFINIR inicioParentesis varTipo variable asig valor finParentesis finLinea 
              | DEFINIR inicioParentesis varTipo variable finParentesis finLinea 
              """
  traductorArduino(p,cb_p_definir)
  pass

def p_varTipo(p):
  """varTipo : int 
          | float 
          | string 
          | bool"""
  pass

def p_valor(p):
  """valor : numero
            | comilla variable comilla
            | true
            | false"""
  pass
def p_reservadas(p):
  """ reservadas : ADEL finFuncion
                | ATR finFuncion
                | IZQ finFuncion
                | DER finFuncion
                | ESP inicioParentesis numero finParentesis finLinea
                | STOP finFuncion"""
  is_first_reserved = True if p_reservadas.counter <= 0 else False
  p_reservadas.counter += 1
  traductorArduino(p,cb_p_reservadas, is_first_reserved=is_first_reserved, is_reserved=True)
  pass
p_reservadas.counter = 0

def p_asignar(p):
  """asignar : variable asig valor finLinea
              | variable asig variable finLinea"""
  traductorArduino(p,cb_p_asignar)
  pass

def p_finFuncion(p):
  """finFuncion : inicioParentesis finParentesis finLinea"""
  pass

def p_predicado(p):
  """predicado : false 
                | true 
                | valor operadorComp valor 
                | inicioParentesis predicado operadorLog predicado finParentesis"""
  pass
def p_operadorLog(p):
  """operadorLog : AND
                  | OR"""
  pass
def p_if(p):
  """if : IF predicado BEGIN cuerpo END else"""
  pass
def p_else(p):
  """else : ELSE BEGIN cuerpo END
          | empty"""
  pass
def p_while(p):
  """while : WHILE predicado BEGIN cuerpo END"""

def p_funcion(p):
  """funcion : FUNC inicioParentesis parametros finParentesis retorno finLinea"""
  traductorArduino(p,cb_p_funcion)
  pass
def p_retorno(p):
  """retorno : dosPuntos varTipo 
              | empty"""
  pass
def p_parametros(p):
  """parametros : varTipo dosPuntos variable 
                | varTipo dosPuntos variable coma parametros
                | empty"""
  pass
def p_empty(p):
  'empty :'
  pass
def p_error(p):
  print("Error sintactico en la linea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')

parser = yacc.yacc() 
analizador.lineno = 0
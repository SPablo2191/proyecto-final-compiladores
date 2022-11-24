import sys
from ply import lex

reserved = {
    "PROGINI" : "PROGINI",
    "PROGFIN" : "PROGFIN",
    "INCLUIR" : "INCLUIR",
    "int" : "int",
    "float" : "float",
    "string" : "string",
    "bool" : "bool",
    "DEFINIR" : "DEFINIR",
    "PIN" :"PIN",
    "DEF" : "DEF",
    "true" : "true",
    "false" : "false",
    "FUNC" : "FUNC",
    "AND" : "AND",
    "OR" : "OR",
    "PIN" : "PIN",
    "SAL" : "SAL",
    "ENT" : "ENT",
    "IF" : "IF",
    "BEGIN" : "BEGIN",
    "ELSE" : "ELSE",
    "END" : "END",
    "WHILE" : "WHILE",
    "ADEL" : "ADEL",
    "ATR" : "ATR",
    "IZQ" : "IZQ",
    "DER" : "DER",
    "ESP" : "ESP",
    "STOP" : "STOP"
}

tokens = [
    "finLinea",
    "coma",
    "operadorAr",
    "operadorComp",
    "inicioParentesis",
    "finParentesis",
    "comilla",
    "saltoLinea",
    "numero",
    "variable",
    "asig",
    "dosPuntos",
    "comLinea",
    "comBloque"
    ] + list(reserved.values())


# Expresiones regulares para tokens 

def t_finLinea(t):
    r'\.'
    return t

def t_coma(t):
    r'\,'
    return t
def t_operadorComp(t):
    r'\>|<|==|!=|<=|>='
    return t
def t_asig(t):
    r':='
    return t
def t_dosPuntos(t):
    r':'
    return t

def t_inicioParentesis(t):
    r'\('
    return t
def  t_finParentesis(t):
    r'\)'
    return t

def t_comilla(t):
    r' \' '
    return t


def t_comLinea(t):
    r'//.*'
    return t

def t_comBloque(t):
    r'{\*.\*}'
    return t

def t_operadorAr(t):
    r'\+ |\- |\*|\/'
    return t

def t_numero(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_space(t):
    r'\s+'
    pass

def t_saltoLinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
  print(f'Error {t.value} en linea {analizador.lineno}')
  t.lexer.skip(1)
    
def t_variable(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value,"variable")
    return t


analizador = lex.lex()

def leerTxt():
    try:
        f = open('data.txt', 'r')
        data = f.read()
        f.close()
        return data
    except:
        sys.stdout.write('Reading from stad  input (tye EOF to end) : \n')
        data = sys.stdin.read()
        return data


analizador.input(leerTxt())

# Identifica tokens
print('Token - Lexema - Linea')
while True:
    tok = analizador.token()
    if not tok:
        break
    print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')
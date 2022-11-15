import sys
from ply import lex

tokens = [
    "progIni",
    "progFin",
    "finLinea",
    "coma",
    "operadorAr",
    "operadorComp",
    "operadorLog",
    "inicioParentesis",
    "finParentesis",
    "comilla",
    "saltoLinea",
    "numero",
    "libExterna",
    "entero",
    "texto",
    "decimal",
    "logico",
    "variable",
    "def",
    "asig",
    "true",
    "false",
    "func",
    "dosPuntos",
    "return",
    "pin",
    "sal",
    "ent",
    "comLinea",
    "comBloque",
    "if",
    "begin",
    "else",
    "end",
    "while",
    "adel",
    "atr",
    "izq",
    "der",
    "esp",
    "stop"
    ]


# Expresiones regulares para tokens simples
t_finLinea = r'\.'
t_coma = r'\,'
t_operadorAr = r'\+ |\- |\*|\/'
t_operadorComp = r'\>|<|==|!=|<=|>='
t_dosPuntos = r':'
t_inicioParentesis = r'\('
t_finParentesis = r'\)'
t_comilla = r' \' '
t_asig = r':='

t_progIni = r'PROGINI'
t_progFin = r'PROGFIN'
t_libExterna = r'INCLUIR'
t_entero = r'int'
t_texto = r'string'
t_decimal = r'float'
t_logico = r'bool'
t_def = r'DEFINIR'
t_true = r'true'
t_false = r'false'
t_func = r'FUNC'
t_return = r'return'
t_operadorLog = r'AND|OR'
t_pin = r'DEF\sPIN'
t_sal = r'SAL'
t_ent = r'ENT'
t_if = r'IF'
t_begin = r'BEGIN'
t_else = r'ELSE'
t_end = r'END'
t_while = r'WHILE'
t_adel = r'ADEL'
t_atr = r'ATR'
t_izq = r'IZQ'
t_der = r'DER'
t_esp = r'ESP'
t_stop = r'STOP'



def t_comLinea(t):
    r'//[a-zA-Z0-9|_ | .|,| ¿ | ? |¡ | ¡ | " | & | ( | ) | { | } | [ | ] |= | \s ]*'
    return t
def t_comBloque(t):
    r'{[a-zA-Z0-9|_ | .|,| ¿ | ? |¡ | ¡ | " | & | ( | ) | { | } | [ | ] |= | \s | \n ]*}'
    return t
def t_numero(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_variable(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
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
    
analizador = lex.lex()

# def leerTxt():
#     try:
#         f = open('data.txt', 'r')
#         data = f.read()
#         f.close()
#         return data
#     except:
#         sys.stdout.write('Reading from stad  input (tye EOF to end) : \n')
#         data = sys.stdin.read()
#         return data


# analizador.input(leerTxt())

# # Identifica tokens
# print('Token - Lexema - Linea')
# while True:
#     tok = analizador.token()
#     if not tok:
#         break
#     print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')
reserved = {
    "progIni" : "PROGINI",
    "progFin" : "PROGFIN",
    "libExterna" : "INCLUIR",
    "entero" : "int",
    "decimal" : "float",
    "texto" : "string",
    "logico" : "bool",
    "def" : "DEFINIR",
    "true" : "true",
    "false" : "false",
    "func" : "FUNC",
    "return" : "return",
    "AND" : "AND",
    "OR" : "OR",
    "pin" : "DEF PIN",
    "sal" : "SAL",
    "ent" : "ENT",
    "if" : "IF",
    "begin" : "BEGIN",
    "else" : "ELSE",
    "end" : "END",
    "while" : "WHILE",
    "adel" : "ADEL",
    "atr" : "ATR",
    "izq" : "IZQ",
    "der" : "DER",
    "esp" : "ESP",
    "stop" : "STOP",

}


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
# t_progIni = r'\PROGINI'
# t_progFin = r'\PROGFIN'
# t_finLinea = r'\'
# t_coma = r'\'
# t_operadorAr = r'\'
# t_operadorComp = r'\'
# t_operadorLog = r'\'
# t_inicioParentesis = r'\'
# t_finParentesis = r'\'

# t_comilla = r'\'
# t_saltoLinea = r'\'
# t_numero = r'\'

# t_libExterna = r'\'
# t_entero = r'\'
# t_texto = r'\'

# t_decimal = r'\'

# t_logico = r'\'

# t_variable = r'\'

# t_def = r'\'
# t_asig = r'\'
# t_true = r'\'
# t_false = r'\'

# t_func = r'\'
# t_dosPuntos = r'\'
# t_return = r'\'

# t_pin = r'\'

# t_sal = r'\'
# t_ent = r'\'

# t_comLinea = r'\'

# t_comBloque = r'\'
# t_if = r'\'

# t_begin = r'\'
# t_else = r'\'
# t_end = r'\'

# t_while = r'\'
# t_adel = r'\'
# t_atr = r'\'
# t_izq = r'\'
# t_der = r'\'
# t_esp = r'\'
# t_stop = r'\'

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


tokens = [
    "t_progIni",
    "t_progFin",
    "t_finLinea",
    "t_coma",
    "t_operadorAr",
    "t_operadorComp",
    "t_operadorLog",
    "t_inicioParentesis",
    "t_finParentesis",
    "t_comilla",
    "t_saltoLinea",
    "t_numero",
    "t_libExterna",
    "t_entero",
    "t_texto",
    "t_decimal",
    "t_logico",
    "t_variable",
    "t_def",
    "t_asig",
    "t_true",
    "t_false",
    "t_func",
    "t_dosPuntos",
    "t_return",
    "t_pin",
    "t_sal",
    "t_ent",
    "t_comLinea",
    "t_comBloque",
    "t_if",
    "t_begin",
    "t_else",
    "t_end",
    "t_while",
    "t_adel",
    "t_atr",
    "t_izq",
    "t_der",
    "t_esp",
    "t_stop"
    ]

def t_comLinea(t):
    r'//[a-zA-Z0-9|_ | .|,| ¿ | ? |¡ | ¡ | " | & | ( | ) | { | } | [ | ] |= | \s ]*'
    return t

def t_comBloque(t):
    r'\{[a-zA-Z0-9|_ | .|,| ¿ | ? |¡ | ¡ | " | & | ( | ) | { | } | [ | ] |= | \s | \n ]*}'
    return t

#·simples
# t_finLinea = r'\.'
# t_coma = r'\,'
# t_operadorAr = r'\+ |\- |\*|\/'
# t_operadorComp = r'\>|<|==|!=|<=|>='
# t_dosPuntos = r':'
# t_inicioParentesis = r'\('
# t_finParentesis = r'\)'
# t_comilla = r' \' '
# t_asig = r':='


# def p_adelante(p):
#   """adelante : ADEL finFuncion"""
#   is_first_operaciones = True if p_adelante.counter <= 0 else False
#   # p_adelante.counter += 1
#   traductorArduino(p,cb_p_operaciones, is_first_reserved=is_first_operaciones, is_reserved=True)
#   pass


# def p_atras(p):
#   """atras : ATR finFuncion"""
#   is_first_operaciones = True if p_atras.counter <= 0 else False
#   # p_adelante.counter += 1
#   traductorArduino(p,cb_p_operaciones, is_first_reserved=is_first_operaciones, is_reserved=True)
#   pass
# def p_izquierda(p):
#   """izquierda : IZQ finFuncion"""
#   is_first_operaciones = True if p_izquierda.counter <= 0 else False
#   # p_adelante.counter += 1
#   traductorArduino(p,cb_p_operaciones, is_first_reserved=is_first_operaciones, is_reserved=True)
#   pass
# def p_derecha(p):
#   """derecha : DER finFuncion"""
#   is_first_operaciones = True if p_derecha.counter <= 0 else False
#   # p_adelante.counter += 1
#   traductorArduino(p,cb_p_operaciones, is_first_reserved=is_first_operaciones, is_reserved=True)
#   pass
# def p_parar(p):
#   """parar : STOP finFuncion"""
#   is_first_operaciones = True if p_parar.counter <= 0 else False
#   # p_adelante.counter += 1
#   traductorArduino(p,cb_p_operaciones, is_first_reserved=is_first_operaciones, is_reserved=True)
#   pass
# def p_esperar(p):
#   """esperar : ESP inicioParentesis numero finParentesis finLinea"""
#   is_first_operaciones = True if p_esperar.counter <= 0 else False
#   # p_adelante.counter += 1
#   traductorArduino(p,cb_p_operaciones, is_first_reserved=is_first_operaciones, is_reserved=True)
#   pass

            #   | adelante cuerpo
            #   | atras cuerpo
            #   | izquierda cuerpo
            #   | derecha cuerpo
            #   | esperar cuerpo
            #   | parar cuerpo
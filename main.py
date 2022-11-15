from analizadorSintactico import parser

filename='data.txt'

try:
    f = open(filename)
    data = f.read()
    f.close()
    print('Contenido del archivo:\n',data,'\n')
except IndexError:
    print('Error en archivo:\n')
    data = ''

try:
    resultado = parser.parse(data)
    print(resultado)
    print('¡Analisis sintactico correcto!')
except:
    print('Analisis sintactico incorrecto')
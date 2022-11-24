from analizadorSintactico import parser

archivo='data.txt'

try:
    f = open(archivo)
    data = f.read()
    f.close()
    print('Data:\n',data,'\n')
except IndexError:
    print('Error en archivo:\n')
    data = ''

try:
    resultado = parser.parse(data)
    print('¡Analisis sintactico correcto!😊')
except Exception as e:
    print(f'Analisis sintactico incorrecto😫 => {e}')




def cb_p_incluir(p):
    list_p = list(p)
    print(list_p)
    result = "".join(["#include <"]+list_p[4:7]+[".h>"]+["\n"])
    return result


def cb_p_definir(p):
    list_p = list(p)
    print(f"hola {list_p}")
    result = "".join([list_p[5]]+[" "]+[list_p[4]]+[";"]+["\n"])
    print(result)
    return result

# def cb_p_reservadas(p):
#   list_cast = list(p)
#   result = "".join([list_cast[1]]+[list_cast[2]]+[list_cast[3]]+[";"]+["\n"])
#   print(result)
#   return result


def cb_p_asignar(p):
    list_p = list(p)
    print(list_p)
    result = "".join([list_p[1]]+[" = "]+[str(list_p[3])]+[";"]+["\n"])
    print(result)
    return result


def cb_p_if(p):
    print(p)
    result = "".join(["if ("]+[") "] + ["{"]+["\n"]+["}"]+["\n"])
    print(result)
    return result


def cb_p_funcion(p):
    list_p = list(p)
    print(list_p)
    result = "".join([list_p[5]]+[list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
    print(result)
    return result


def cb_p_predicado(p):
    list_p = list(p)
    print(list_p)
    result = "".join([list_p[5]]+[" "]+[list_p[3]] +
                     ["("]+[list_p[7]]+[");"]+["\n"])
    print(result)
    return result


def cb_p_pin(p):
    list_p = list(p)
    print(list_p)
    result = "".join(
        ["pinMode("]+[list_p[4]]+[" , "]+[list_p[4]]+[" );"]+["\n"])
    print(result)
    return result


def cb_p_reservadas(p):
    list_p = list(p)
    print(list_p[1])
    if list_p[1] == 'ADEL':
      print('entro')
      return 'avanzar();'+"\n"
    elif list_p[1] == 'ATR':
      return 'retroceder();'+"\n"
    elif list_p[1] == 'IZQ':
      return 'giro_izquierda();'+"\n"
    elif list_p[1] == 'DER':
      return 'giro_derecha();'+"\n"
    elif list_p[1] == 'ESP':
      return 'esperar();'+"\n"
    elif list_p[1] == 'STOP':
      return 'parar();'+"\n"

# if __name__ == "__main__":
#   res = cb_p_incluir([None, 'extend', '(', 'nombreDeLibreria', '.txt', ')', ';', None])

#   res1 = cb_p_definir([None, 'VBLE', '(', 'MD1', ':', 'int', ')', ';'])
#   print(res1)

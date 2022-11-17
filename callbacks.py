def cb_p_incluir(p):
    list_p = list(p)
    result = "".join(["#include \""]+list_p[3:4]+[".h\""]+["\n"])
    return result 

def cb_p_definir(p):
  list_p = list(p)
  result = "".join([list_p[5]]+[" "]+[list_p[3]]+[";"]+["\n"])
  return result

def cb_p_asignar(p):
  list_p = list(p)
  result = "".join([list_p[1]]+[" = "]+[str(list_p[3])]+[";"]+["\n"])
  return result

def cb_p_if(p):
  result = "".join(["if ("]+[") "]+ ["{"]+["\n"]+["}"]+["\n"])
  return result


def cb_p_funcion(p):
  list_p = list(p)
  result = "".join([list_p[5]]+[list_p[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_predicado(p):
  list_p = list(p)
  result = "".join([list_p[5]]+[" "]+[list_p[3]]+["("]+[list_p[7]]+[");"]+["\n"])
  return result


def cb_p_pin(p):
   list_p = list(p)
   result = "".join(["pinMode("]+[list_p[3]]+[" , "]+[list_p[5]]+[" );"]+["\n"])
   return result

def cb_p_operaciones(p):
  list_p = list(p)
  return "".join([list_p[1]]+[list_p[2]]+[list_p[3]]+[";"]+["\n"])

# if __name__ == "__main__":
#   res = cb_p_incluir([None, 'extend', '(', 'nombreDeLibreria', '.txt', ')', ';', None])

#   res1 = cb_p_definir([None, 'VBLE', '(', 'MD1', ':', 'int', ')', ';'])
#   print(res1)
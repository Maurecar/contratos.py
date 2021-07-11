def determinar_tipo_contrato(data):
    result = []
    for i in data:
        if i not in result:
            result.append(i)
        
    return result

def buscar_mas_informacion(a, b, c):
    m=[i for i, x in enumerate(b) if x== c]
    s = comprar_informacion(a, m)
    return s
    
def comprar_informacion(a, b):
    result  = []
    for i in a:
        if not i in b:
            result.append(i) 
    
    return result
def intercambiar_informacion(a, b):
    calculo = 0
   
    for i in b:
        if not i in a:
            calculo += 1
           
    return calculo

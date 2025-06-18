

def api (endpoint):
    """
    Función para acceder a la información de la base de datos utilizando un endpoint dado.
    Recibe:
    -endpoint :str
    Retorna:
    -data: dic[]
    """
    
    #se hcae el request a la base de datos
    response = requests.request ('GET', endpoint)
    
    #se transforma esa respuesta en un diccionario 
    dictionary = response.json ()
    
    #se retorna el diccionario
    return dictionary 
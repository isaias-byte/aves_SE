def formatoRespuestas(preguntas):
    temp = {
        'ojos': '',
        'pico': '',
        'antifaz': '',
        'frente': '',
        'loras': '',
        'cuerpo': '',
        'nuca': '',
        'auriculares': '',
        'pecho': '',
        'vientre': '',
        'cabeza': '',
        'garganta': '',
        'espalda': '',
        'alas': '',
        'cola': '',
        'patas': '',
        'tarso': '',
        'rabadilla': '',
        'tamanio': '',
        'habitat': '',
        'comida': ''
    }
    
    for clave, valor in preguntas.items():
        temp[clave] = [valor] if (valor != '' and valor != 'x') else []
    
    return temp
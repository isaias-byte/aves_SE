# Convierte las respuestas a un diccionario para después integrarlas al archivo json
def formatoRespuestas(preguntas):
    respuestas = {
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
        respuestas[clave] = [valor] if (valor != '' and valor != 'x') else []
    
    return respuestas

# Búsqueda del ave
def buscarAve(preguntas, data):
    avesResultado = list()
    
    for ave, contenido in data.items():
        if (
            ((preguntas.get('ojos') in contenido.get('ojos')) or (preguntas.get('ojos') == 'x') or (preguntas.get('ojos') == '')) and
            ((preguntas.get('pico') in contenido.get('pico')) or (preguntas.get('pico') == 'x') or (preguntas.get('pico') == '')) and
            ((preguntas.get('alas') in contenido.get('alas')) or (preguntas.get('alas') == 'x') or (preguntas.get('alas') == '')) and
            ((preguntas.get('cola') in contenido.get('cola')) or (preguntas.get('cola') == 'x') or (preguntas.get('cola') == '')) and
            ((preguntas.get('espalda') in contenido.get('espalda')) or (preguntas.get('espalda') == 'x') or (preguntas.get('espalda') == '')) and
            ((preguntas.get('pecho') in contenido.get('pecho')) or (preguntas.get('pecho') == 'x') or (preguntas.get('pecho') == '')) and
            ((preguntas.get('patas') in contenido.get('patas')) or (preguntas.get('patas') == 'x') or (preguntas.get('patas') == '')) and
            ((preguntas.get('cabeza') in contenido.get('cabeza')) or (preguntas.get('cabeza') == 'x') or (preguntas.get('cabeza') == '')) and
            ((preguntas.get('cuerpo') in contenido.get('cuerpo')) or (preguntas.get('cuerpo') == 'x') or (preguntas.get('cuerpo') == '')) and
            ((preguntas.get('frente') in contenido.get('frente')) or (preguntas.get('frente') == 'x') or (preguntas.get('frente') == ''))
            ):
                avesResultado.append(ave)
    
    return avesResultado
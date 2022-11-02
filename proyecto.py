from aves import aves
import json
import random

# Escribir el diccionario de aves a un archivo json
# with open('aves.json', 'w', encoding="utf-8") as outfile:
#     json.dump(aves, outfile)

# Leer el archivo json de aves para convertirlo en un diccionario
data = dict()
with open('aves.json') as json_file:
    data = json.load(json_file)   # Obtiene el contenido del archivo json y lo convierte a un diccionario

print('\n')
print('------------------------------------------')
print('---------- CLASIFICADOR DE AVES ----------')
print('------------------------------------------')
print('\n')

print('A continuación se te realizarán una serie de preguntas,')
print('en caso de no saber la respuesta puedes responder con una "x"\n')

# Arreglo de opciones de preguntas, el cual cuenta con las características de las aves
opciones = [
    'ojos',
    'pico',
    'alas',
    'cola',
    'espalda',
    'pecho',
]

# Diccionario en el que se almacenan las respuestas proporcionadas por el usuario
preguntas = {
    'ojos': '',
    'pico': '',
    'alas': '',
    'cola': '',
    'espalda': '',
    'pecho': '',
    'patas': '',
    'cabeza': '',
    'cuerpo': '',
    'frente': '',
}

# Preguntas aleatorias
while len(opciones) > 0:
    aleatorio = random.randint(0, len(opciones) - 1)   # Obtiene un número entre 0 y la longitud del arreglo
    opcion = opciones.pop(aleatorio)                   # Se quita ese índice del arreglo de opciones de preguntas
    res = input('Color de ' + opcion + ': ').lower()   # Guarda el resultado que el usuario captura en pantalla
    preguntas[opcion] = res                            # Asigna el resultado al índice del diccionario de preguntas

# Mostrar todas las aves
# for ave, contenido in aves.items():
#     print('------------------------------')
#     print(ave, ':')
#     for caracteristica, valor in contenido.items():
#         print(caracteristica, ':', valor, ',', len(valor))
#     print('------------------------------')
#     print('\n')

# Mostrar todo lo que capturó el usuario
print('\n\nTu búsqueda fue la siguiente:')
for clave, valor in preguntas.items():
    print(clave, ':', valor)
print('\n')

avesResultado = list()

# Búsqueda del ave
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

# Posibles resultados
if(len(avesResultado) == 1):   # Ave encontrada
    for ave, contenido in aves.items():
        if(avesResultado[0] == ave):   # Obtener los datos del ave desde el diccionario
            ave = ave.replace('_', ' ').title()   # Convertir el nombre del ave a mayúsculas y eliminar los guiones bajos
            print('El ave que buscas es:', ave)
            descripcion = 'El ave ' + ave + ' se caracteriza por tener '
            for caracteristica, valor in contenido.items():        # Obtener las características del ave
                if(preguntas.__contains__(caracteristica) and preguntas.get(caracteristica) != 'x' and preguntas.get(caracteristica) != ''):
                    colores = len(valor)   # Cantidad de colores en dicha característica
                    if colores == 2:
                        descripcion += caracteristica + ' color ' + ' y '.join(valor) + ', '
                    elif colores > 2:
                        valorAux = ''
                        for i, color in enumerate(valor):
                            if i == colores - 1:
                                valorAux += ' y ' + color
                            else:
                                if i == 0:
                                    valorAux += color
                                else:
                                    valorAux += ', ' + color

                        descripcion += caracteristica + ' color ' + valorAux + ', '
                    else:
                        descripcion += caracteristica + ' color ' + valor[0] + ', '
                        
            descripcion = descripcion[:-2]   # Obtiene los últimos dos caracteres de la cadena
            descripcion += '.\n'
            # Información adicional del ave
            descripcion += 'Como dato adicional, esta ave mide ' + str(contenido.get('tamanio')[0]) + ' cm y la puedes encontrar en lugares como ' + ''.join(contenido.get('habitat')) + '.\n'
            descripcion += 'Además, se alimenta principalmente de ' + ''.join(contenido.get('comida')) + '.\n'
            print(descripcion)
            break
        
elif(len(avesResultado) == 0):   # No se encontraron coincidencias
    print('No pudimos encontrar el ave que buscas :(\n')
    print("¿Quieres añadir esta nueva?")
    print("1) Sí")
    print("2) No")
    opc = input('Escoge una opción: ')
    
    while True:
        if opc == '1':
            # data.append()
            # with open('aves.json', "w") as file:
            #     json.dump(data, file)
            # break
            pass
        elif opc == '2':
            print('Nos vemos... :)')
            break
        else:
            print('Escoge una opción válida')
            
elif(len(avesResultado) > 1):   # Se encontró más de una coincidencia
    print('La ave que buscas puede ser una de las siguientes:\n')
    for ave in avesResultado:
        ave = ave.replace('_', ' ').title()
        print(ave)
    print('\n')
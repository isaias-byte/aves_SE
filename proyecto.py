from aves import aves
from funciones import *
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
print('-----------------------------------------------')
print('----------- CLASIFICADOR DE AVES SEBC ---------')
print('-----------------------------------------------')
print('\n')

print('A continuación se te realizarán una serie de preguntas,')
print('en caso de no saber la respuesta puedes responder con una "x"')
print('o sino simplemente dando enter a la pregunta.\n')

# Arreglo de opciones de preguntas, el cual cuenta con las características de las aves
opciones = [
    'ojos',
    'pico',
    'alas',
    'cola',
    'espalda',
    'pecho',
    'patas',
    'cabeza',
    'cuerpo',
    'frente',
]

# Diccionario en el que se almacenan las respuestas proporcionadas por el usuario
preguntas = {
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

# Preguntas aleatorias
while len(opciones) > 0:
    aleatorio = random.randint(0, len(opciones) - 1)   # Obtiene un número entre 0 y la longitud del arreglo
    opcion = opciones.pop(aleatorio)                   # Se quita ese índice del arreglo de opciones de preguntas
    res = input('Color de ' + opcion + ': ').lower()   # Guarda el resultado que el usuario captura en pantalla
    preguntas[opcion] = res                            # Asigna el resultado al índice del diccionario de preguntas
    
    avesResultado = buscarAve(preguntas, data)         # Busca al ave cada vez que se responde a una pregunta
    if(len(avesResultado) == 1):                       # Ave encontrada
        break

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
    if valor != '' and valor != 'x':   # Obtiene solo las respuestas proporcionadas por el usuario
        print(clave, ':', valor)
print('\n')

# Posibles resultados
if(len(avesResultado) == 1):   # Ave encontrada
    for ave, contenido in data.items():
        if(avesResultado[0] == ave):   # Obtener los datos del ave desde el diccionario
            ave = ave.replace('_', ' ').title()   # Convertir el nombre del ave a mayúsculas y eliminar los guiones bajos
            print('El ave que buscas es:', ave)
            descripcion = 'El ave ' + ave + ' se caracteriza por tener '
            for caracteristica, valor in contenido.items():   # Obtener las características del ave
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
            if len(contenido.get('tamanio')) != 0 or len(contenido.get('habitat')) != 0 or len(contenido.get('comida')) != 0:
                descripcion += 'Como dato adicional, esta ave '
                if len(contenido.get('tamanio')) != 0:
                    descripcion += 'mide ' + str(contenido.get('tamanio')[0]) + ' cm'
                    if len(contenido.get('habitat')) == 0:
                        descripcion += '.\n'
                
                if len(contenido.get('habitat')) != 0:
                    if len(contenido.get('tamanio')) != 0:
                        descripcion += ' y la puedes encontrar en lugares como ' + ''.join(contenido.get('habitat')) + '.\n'
                    else:
                        descripcion += ' la puedes encontrar en lugares como ' + ''.join(contenido.get('habitat')) + '.\n'
                
                if(len(contenido.get('comida')) != 0):
                    if(len(contenido.get('tamanio')) != 0 or len(contenido.get('habitat')) != 0):
                        descripcion += 'Además, se alimenta principalmente de ' + ''.join(contenido.get('comida')) + '.\n'
                    else:
                        descripcion += ' se alimenta principalmente de ' + ''.join(contenido.get('comida')) + '.\n'
            
            print(descripcion)
            break
        
elif(len(avesResultado) == 0):   # No se encontraron coincidencias
    print('No pudimos encontrar el ave que buscas :(\n')
    print('¿Quieres añadir esta nueva?')
    print('1) Sí')
    print('2) No')
    opc = input('Escoge una opción: ')
    
    while True:
        if opc == '1':
            nuevaAve = input('\nNombre de la nueva ave: ')
            nuevaAve = nuevaAve.replace(' ', '_').lower()   # Convertir el nombre del ave a minúsculas y poner guiones bajos entre cada espacio
            
            # Captura de últimos datos para el alta del ave
            print('\nPara finalizar el alta de esta nueva ave, ayúdanos contestando las siguientes preguntas.')
            print('En caso de que no conozcas el dato, puedes omitirlas dando enter o escribiendo una "x".\n')
            preguntas['tamanio'] = input('\n¿Qué tamaño tiene el ave en centímetros?: ')
            preguntas['habitat'] = input('¿Dónde se puede ubicar a esta ave?: ')
            preguntas['comida'] = input('¿Qué suele comer el ave?: ')
            
            respuestas = formatoRespuestas(preguntas)
            data[nuevaAve] = respuestas   # Agrega el ave al diccionario de aves
            with open('aves.json', "w") as file:
                json.dump(data, file)     # Escribe el ave capturada en el archivo json
            print('\nAve agregada exitosamente...\n')
            break
        elif opc == '2':
            print('Nos vemos... :)\n')
            break
        else:
            print('Escoge una opción válida')
            
elif(len(avesResultado) > 1):   # Se encontró más de una coincidencia
    print('La ave que buscas puede ser una de las siguientes:\n')
    for ave in avesResultado:
        ave = ave.replace('_', ' ').title()
        print(ave)
    print('\n')
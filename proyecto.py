from aves import aves

# ojos: negros (example)
# loras: negras (example
# nuca: naranja (example)
# auriculares: grises
# alas: rojas
# cola: roja
# patas: amarillas
# rabadilla: amarilla

print('\n')
print('------------------------------------------')
print('---------- CLASIFICADOR DE AVES ----------')
print('------------------------------------------')
print('\n')

print('A continuación se te realizarán una serie de preguntas,')
print('en caso de no saber la respuesta puedes responder con una "x"\n')

print('\nPreguntas:')
ojos = input('Color de ojos: ').lower()
pico = input('Color de pico: ').lower()
alas = input('Color de alas: ').lower()
cola = input('Color de cola: ').lower()

preguntas = {
    'ojos': ojos,
    'pico': pico,
    'alas': alas,
    'cola': cola,
}

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

for ave, contenido in aves.items():
    if (
        ((preguntas.get('ojos') in contenido.get('ojos')) or (preguntas.get('ojos') == 'x')) and
        ((preguntas.get('pico') in contenido.get('pico')) or (preguntas.get('pico') == 'x')) and
        ((preguntas.get('alas') in contenido.get('alas')) or (preguntas.get('alas') == 'x')) and
        ((preguntas.get('cola') in contenido.get('cola')) or (preguntas.get('cola') == 'x'))
        ):
            avesResultado.append(ave)
    
if(len(avesResultado) == 1):
    for ave, contenido in aves.items():
        if(avesResultado[0] == ave):
            print('La ave que buscas es:', ave)
            print('\nEsta ave tiene:\n')
            for caracteristica, valor in contenido.items():
                print(caracteristica, ':', valor)
            print('\n')
            break
elif(len(avesResultado) == 0):
    print('No pudimos encontrar el ave que buscas :(\n')
elif(len(avesResultado) > 1):
    print('La ave que buscas puede ser una de estas:\n')
    for ave in avesResultado:
        print(ave)
    print('\n')
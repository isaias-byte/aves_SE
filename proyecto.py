from aves import aves

# ojos: negros (example)
# loras: negras (example
# nuca: naranja (example)
# auriculares: grises
#alas: rojas
#cola: roja
# patas: amarillas
#rabadilla: amarilla

print('\n')
print('------------------------------------------')
print('---------- CLASIFICADOR DE AVES ----------')
print('------------------------------------------')
print('\n')


print('Preguntas')
ojos = input('Color de ojos: ')
pico = input('Color de pico: ')
alas = input('Color de alas: ')
cola = input('Color de cola: ')

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
print('\n')
for clave, valor in preguntas.items():
    print(clave, ':', valor)

print('\n')

avesResultado = dict()

for ave, contenido in aves.items():
    if (
        (preguntas.get('ojos') in contenido.get('ojos')) and
        (preguntas.get('pico') in contenido.get('pico')) and
        (preguntas.get('alas') in contenido.get('alas')) and
        (preguntas.get('cola') in contenido.get('cola'))
        ):
            print('------------------------------')
            print(ave, ':')
            for caracteristica, valor in contenido.items():
                print(caracteristica, ':', valor, ',', len(valor))
            print('------------------------------')
            print('\n')
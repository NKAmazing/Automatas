import re
def contiene_mayus(cadena):
    patron = '#'
    if re.search(patron, cadena[0]):
        print(f'La cadena "{cadena}" si es valido en python porque contiene el patron: "{patron}"')
    else:
        print(f'La cadena "{cadena}" no es valido en python porque no contiene el patron: "{patron}"')

cadena_1 = '#juan123'
cadena_2 = 'Nico1'
cadena_3 = 'sA#ntiago'

contiene_mayus(cadena_1)
contiene_mayus(cadena_2)
contiene_mayus(cadena_3)
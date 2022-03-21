import re
def contiene_mayus(cadena):
    patron = '[A-Z]'
    if re.search(patron, cadena[0]):
        print(f'La cadena "{cadena}" contiene una mayuscula del patron: "{patron}"')
    else:
        print(f'La cadena "{cadena}" no contiene una mayuscula del patron: "{patron}"')

cadena_1 = 'juan'
cadena_2 = 'Nico'
cadena_3 = 'sAntiago'

contiene_mayus(cadena_1)
contiene_mayus(cadena_2)
contiene_mayus(cadena_3)
import re
def contiene_mayus(cadena):
    patron = '[0-9]'
    if re.search(patron, cadena):
        print(f'La cadena "{cadena}" contiene un numero del: "{patron}"')
    else:
        print(f'La cadena "{cadena}" no contiene un numero del: "{patron}"')

cadena_1 = 'juan123'
cadena_2 = 'Nico1'
cadena_3 = 'sAntiago'

contiene_mayus(cadena_1)
contiene_mayus(cadena_2)
contiene_mayus(cadena_3)
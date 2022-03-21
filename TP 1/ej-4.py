import re
def contiene(cadena):
    patron = '[7]'
    patron_2 = '[p, P]'
    if re.search(patron, cadena[0]):
        print(f'La cadena "{cadena}" contiene en su inicio el numero: "{patron}"')
    else:
        print(f'La cadena "{cadena}" no contiene en su inicio el numero: "{patron}"')

    if re.search(patron_2, cadena):
        print(f'La cadena "{cadena}" contiene la letra: "{patron_2}"')
    else:
        print(f'La cadena "{cadena}" no contiene la letra: "{patron_2}"')

cadena_1 = '7juan123'
cadena_2 = 'Nico1'
cadena_3 = 'sA#nptiago'

contiene(cadena_1)
contiene(cadena_2)
contiene(cadena_3)
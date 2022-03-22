import re
import string
def contiene_s(cadena):
    patron = '[7]'
    patron_n = '[0-9]'
    patron_1 = '[a-z A-Z]'
    patron_2 = '[p, P]'


    if re.search(patron_n, cadena[0]):
        print(f'"{cadena}" empieza con numero.')


        if re.search(patron, cadena[0]):
            print(f'La cadena "{cadena}" contiene en su inicio el numero: "{patron}"')
        else:
            print(f'La cadena "{cadena}" no contiene en su inicio el numero: "{patron}"')


    elif re.search(patron_1, cadena[0]):
        print(f'"{cadena}" empieza con una letra del patron: "{patron_1}"')
        

        if re.search(patron_2, cadena[0]):
            print(f'La cadena "{cadena}" contiene la letra: "{patron_2}" en su inicio.')
        else:
            print(f'La cadena "{cadena}" no contiene la letra: "{patron_2}" en su inicio.')


cadena_1 = '7juan123'
cadena_2 = 'Nico1'
cadena_3 = 'sA#nptiago'
cadena_4 = '8alexis'
cadena_5 = 'pedro'

contiene_s(cadena_1)
contiene_s(cadena_2)
contiene_s(cadena_3)
contiene_s(cadena_4)
contiene_s(cadena_5)
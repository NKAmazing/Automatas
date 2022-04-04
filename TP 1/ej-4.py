import re
import string
def contiene_s(cadena):
    patron = '[7]'
    patron_n = '[0-9]'
    patron_1 = '[a-z A-Z]'
    patron_2 = '[p, P]'


    if re.search(patron_n, cadena[0]):
        print(f'"{cadena}" empieza con numero.')


        if re.search(patron, cadena):
            print(f'La cadena "{cadena}" contiene el numero: "{patron}"')
        else:
            print(f'La cadena "{cadena}" no contiene el numero: "{patron}"')


    elif re.search(patron_1, cadena[0]):
        print(f'"{cadena}" empieza con una letra del patron: "{patron_1}"')
        

        if re.search(patron_2, cadena):
            print(f'La cadena "{cadena}" contiene la letra: "{patron_2}"')
        else:
            print(f'La cadena "{cadena}" no contiene la letra: "{patron_2}"')


cadena_1 = input('Ingrese cadena: ')

contiene_s(cadena_1)
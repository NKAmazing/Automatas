import time

def main():
    print("Ingrese cualquier tipo de cadena del formato: (aa|b)*(a|bb)*")
    # ingreso una cadena compatible con el automata
    string = str(input("Ingrese cadena: "))
    # llamo a la funcion para que haga la transicion de estados
    transition_process(string)

def transition_process(string):
    # inicializo el estado
    state = 0
    print(f"Ha introducido: '{string}'")
    print("INICIANDO AUTOMATA...")
    print("ESTADO INICIAL: ", state)
    # analizo con un for las transiciones de estado, recorriendo la cadena de entrada
    for i in range(len(string)):
        # igualo la posicion de la cadena en la que estoy a la transicion actual
        transition = string[i]
        # analizo con un if cada estado importante
        # itero con el estado 6
        if state == 6:
            plus = 1
            next = find_next_value(string, i, plus)
            # analizo la transicion a
            if transition == 'a':
                # si el siguiente tambien es un a, entonces cambia a estado 0
                if next == 'a':
                    state = 0
                    print("ESTADO: ", state)
                    time.sleep(1)
                # si el siguiente no es un a, hace la transicion de 7 a 8 a 12
                else:
                    state = 7
                    print("ESTADO: ", state)
                    state = 8
                    print("ESTADO: ", state)
                    time.sleep(1)
                    state = 12
                    print("ESTADO: ", state)
                    time.sleep(1)
            # analizo la transicion b
            elif transition == 'b':
                # si el siguiente tambien es un b, entonces hace la transicion de 9 a 10 y continua el ciclo for
                if next == 'b':
                    state = 9
                    print("ESTADO: ", state)
                    state = 10
                    print("ESTADO: ", state)
                    time.sleep(1)
                    continue
                # si el siguiente tambien es un a, entonces cambia a estado 0
                elif next == 'a':
                    state = 0
                    print("ESTADO: ", state)
                # si no es ninguno de los dos, cambia a 0 y continua el ciclo for
                else:
                    state = 0
                    print("ESTADO: ", state)
                    continue
            # analizo la transicion vacia
            elif transition == '':
                # analizo el siguiente del siguiente con la funcion
                plus = 2
                next_2 = find_next_value(string, i, plus)
                # si el siguiente es a, y el siguiente a ese es a tambien, cambia a estado 0
                if next == 'a':
                    if next_2 == 'a':
                        state = 0
                        print("ESTADO: ", state)
                        continue
                    # si no, error en la cadena, no pertenece a este automata
                    else:
                        print("ERROR en la cadena")
                # si el siguiente es b
                elif next == 'b':
                    # si el siguiente a ese es 0, cambia a estado 0
                    if next_2 == 0:
                        state = 0
                        print("ESTADO: ", state)
                        continue
                    # si no, error en la cadena, no pertenece a este automata
                    else:
                        print("ERROR en la cadena")
                # si no es b, cambia a estado 12
                else:
                    state = 12
                    print("ESTADO: ", state)
        # itero con el estado 0
        if state == 0:
            plus = 1
            next = find_next_value(string, i, plus)
            # si la transicion es a, cambia de estado 0 a 1 y luego a 2 y continua el ciclo del for
            if transition == 'a':
                state = 1
                print("ESTADO: ", state)
                state = 2
                print("ESTADO: ", state)
                time.sleep(1)
                continue
            # si la transicion es b, cambia de estado 0 a 4 a 5 y termina en 6, despues continua el ciclo del for
            elif transition == 'b':
                state = 4
                print("ESTADO: ", state)
                state = 5
                print("ESTADO: ", state)
                time.sleep(1)
                state = 6
                print("ESTADO: ", state)
                continue
            # si la transicion es vacia, pasa a estado 6 directamente
            elif transition == ' ':
                state = 6
                print("ESTADO: ", state)
                print("Estado de aceptacion alcanzado")
            # si no es ninguna de esas transiciones, tira error en la cadena
            else:
                print("ERROR en la cadena")
                return
        # itero con el estado 2
        if state == 2:
            # si la transicion es a, cambia de estado 2 a 3 y pasa a 6, luego continua el ciclo del for
            if transition == 'a':
                state = 3
                print("ESTADO: ", state)
                time.sleep(1)
                state = 6
                print("ESTADO: ", state)
                continue
            # si es cualquier otra cosa, tira error en la cadena
            else:
                print("ERROR en la cadena")
                return

        # itero con el estado 10
        if state == 10:
            # si la transicion es b, cambia de estado 10 a 11 y llega a 12
            if transition == 'b':
                state = 11
                print("ESTADO: ", state)
                state = 12
                print("ESTADO: ", state)
            # si es cualquier otra cosa, tira error en la cadena
            else:
                print("ERROR en la cadena")
                return
        # itero con el estado 12
        if state == 12:
            # analiza si es el ultimo elemento de la cadena, en cuyo caso, llega a estado de aceptacion
            if i == (len(string) - 1):
                print("Estado de aceptacion alcanzado")
            # si no es el ultimo, vuelve al 6
            else:
                state = 6
                print("ESTADO: ", state)

# defino una funcion que analiza los elementos siguientes de la cadena
def find_next_value(string, i, plus):
    try:
        return string[i + plus]
    except:
        return 0
# defino el constructor, para ejecutar el main()
if __name__ == '__main__':
    main()


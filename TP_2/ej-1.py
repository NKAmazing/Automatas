import time

def main():
    print("Ingrese cualquier tipo de cadena del formato: (a|b)*")
    # defino una cadena de entrada
    string = str(input("Ingrese cadena: "))
    # llamo a la funcion
    transition_process(string)

def transition_process(string):
    # inicializo el estado en 0
    state = 0
    print(f"Ha introducido: '{string}'")
    print("INICIANDO AUTOMATA...")
    print("ESTADO INICIAL: ", state)
    # recorro la cadena de entrada con un for
    for i in range(len(string)):
        # igualo la cadena de la posicion actual a la transicion
        transition = string[i]
        # itero con un if, si el estado es 0
        if state == 0:
            # si la transicion es a, cambia de estado 0 a 1 y luego a 2
            if transition == 'a':
                state = 1
                print("ESTADO: ", state)
                state = 2
                print("ESTADO: ", state)
                time.sleep(1)
            # si la transicion es b, cambia de estado 0 a 3 y luego a 4
            elif transition == 'b':
                state = 3
                print("ESTADO: ", state)
                state = 4
                print("ESTADO: ", state)
                time.sleep(1)
            # si la transicion es vacia, pasa a estado 5 directamente
            elif transition == 'E':
                state = 5
                print("ESTADO: ", state)
            # si no, tira error
            else:
                print("ERROR")
        # itero con un if, si el estado es 2 o 4, cambio a estado 5
        if state == 2 or state == 4:
                state = 5
                print("ESTADO: ", state)
                time.sleep(1)
        # itero con un if, si el estado es el 5, analiza si es el ultimo elemento de la cadena
        if state == 5:
            if i == (len(string) - 1):
                print("Estado de aceptacion alcanzado")
            # si no lo es, vuelve a estado 0
            else:
                state = 0
                print("ESTADO: ", state)
                time.sleep(1)
# defino el constructor para ejecutar el main()
if __name__ == '__main__':
    main()
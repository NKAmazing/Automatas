import time

def main():
    print("Ingrese cualquier tipo de cadena del formato: (a|b)*")
    string = str(input("Ingrese cadena: "))
    transition_process(string)

def transition_process(string):
    state = 0
    print(f"Ha introducido: '{string}'")
    print("INICIANDO AUTOMATA...")
    print("ESTADO INICIAL: ", state)
    for i in range(len(string)):
        transition = string[i]
        if state == 0:
            if transition == 'a':
                state = 1
                print("ESTADO: ", state)
                state = 2
                print("ESTADO: ", state)
                time.sleep(1)
            elif transition == 'b':
                state = 3
                print("ESTADO: ", state)
                state = 4
                print("ESTADO: ", state)
                time.sleep(1)
            elif transition == 'E':
                state = 5
                print("ESTADO: ", state)
            else:
                print("ERROR")
        if state == 2 or state == 4:
                state = 5
                print("ESTADO: ", state)
                time.sleep(1)
        if state == 5:
            if i == (len(string) - 1):
                print("Estado de aceptacion alcanzado")
            else:
                state = 0
                print("ESTADO: ", state)
                time.sleep(1)

if __name__ == '__main__':
    main()
import time

def main():
    print("Ingrese cualquier tipo de cadena del formato: (aa|b)*(a|bb)*")
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
                continue
            elif transition == 'b':
                state = 4
                print("ESTADO: ", state)
                state = 5
                print("ESTADO: ", state)
                time.sleep(1)
                state = 6
            elif transition == 'E':
                state = 6
                print("ESTADO: ", state)
                print("Estado de aceptacion alcanzado")
            else:
                print("ERROR")
        if state == 2:
            if transition == 'a':
                state = 3
                print("ESTADO: ", state)
                time.sleep(1)
                state = 6
                print("ESTADO: ", state)
            else:
                print("ERROR en la cadena")
        if state == 6:
            next = string[i + 1]
            if transition == 'a':
                if next == 'a':
                    state = 7
                    print("ESTADO: ", state)
                    state = 8
                    print("ESTADO: ", state)
                    time.sleep(1)
                    state = 12
                    print("ESTADO: ", state)
                    time.sleep(1)
                else:
                    state = 0
                    print("ESTADO: ", state)
                    time.sleep(1)
            if transition == 'b':
                if next == 'b':
                    state = 9
                    print("ESTADO: ", state)
                    state = 10
                    print("ESTADO: ", state)
                    time.sleep(1)
                    continue
                else:
                    state = 0
                    print("ESTADO: ", state)
                    
            if i == (len(string) - 1):
                print("Estado de aceptacion alcanzado")
        if state == 10:
            print("ESTADO: ", state)
            if transition == 'b':
                state = 11
                print("ESTADO: ", state)
                state = 12
                print("ESTADO: ", state)
            else:
                print("ERROR")

        if state == 12:
            if i == (len(string) - 1):
                print("Estado de aceptacion alcanzado")
            else:
                state = 6
                print("ESTADO: ", state)

            
            
if __name__ == '__main__':
    main()


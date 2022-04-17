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
        if state == 6:
            plus = 1
            next = find_next_value(string, i, plus)
            if transition == 'a':
                if next == 'a':
                    state = 0
                    print("ESTADO: ", state)
                    time.sleep(1)
                else:
                    state = 7
                    print("ESTADO: ", state)
                    state = 8
                    print("ESTADO: ", state)
                    time.sleep(1)
                    state = 12
                    print("ESTADO: ", state)
                    time.sleep(1)

            elif transition == 'b':
                if next == 'b':
                    state = 9
                    print("ESTADO: ", state)
                    state = 10
                    print("ESTADO: ", state)
                    time.sleep(1)
                    continue
                elif next == 'a':
                    state = 0
                    print("ESTADO: ", state)
                else:
                    state = 0
                    print("ESTADO: ", state)
                    continue
        
            elif transition == '':
                plus = 2
                next_2 = find_next_value(string, i, plus)
                if next == 'a':
                    if next_2 == 'a':
                        state = 0
                        print("ESTADO: ", state)
                        continue
                    else:
                        print("ERROR en la cadena")
                elif next == 'b':
                    if next_2 == 0:
                        state = 0
                        print("ESTADO: ", state)
                        continue
                    else:
                        print("ERROR en la cadena")
                else:
                    state = 12
                    print("ESTADO: ", state)

        if state == 0:
            
            plus = 1
            next = find_next_value(string, i, plus)
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
                print("ESTADO: ", state)
                continue
            elif transition == ' ':
                state = 6
                print("ESTADO: ", state)
                print("Estado de aceptacion alcanzado")
            else:
                print("ERROR en la cadena")
                return

        if state == 2:
            if transition == 'a':
                state = 3
                print("ESTADO: ", state)
                time.sleep(1)
                state = 6
                print("ESTADO: ", state)
                continue
            else:
                print("ERROR en la cadena")
                return


        if state == 10:
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

def find_next_value(string, i, plus):
    try:
        return string[i + plus]
    except:
        return 0

if __name__ == '__main__':
    main()


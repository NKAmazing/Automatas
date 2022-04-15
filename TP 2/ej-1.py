import time

def main():
    input_1 = input(str("Ingrese cadena: "))
    list_1 = list(input_1)
    global state
    state = 0
    state_transition(list_1)

def state_transition(list_1):
    print("Iniciando automata...")
    for i in range(len(list_1)):
        if list_1[i] == 'a':
            transition_a()
        elif list_1[i] == 'b':
            
            transition_b()
        elif list_1[i] == "":
            end_process()
        else:
            print("ERROR: Cadena incorrecta")
    end_process()
            
def transition_a():
    state = 1
    print("ESTADO: ", state)
    state = 2
    print("ESTADO: ", state)
    time.sleep(1)

def transition_b():
    state = 3
    print("ESTADO: ", state)
    state = 4
    print("ESTADO: ", state)
    time.sleep(1)

def end_process():
    state = 5
    print("ESTADO: ", state)
    print("Estado de aceptacion alcanzado")

main()

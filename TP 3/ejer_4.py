# Ejercicio 4 (en clase) - TP3 - Automata: (a|b)*(a|bb)

from asyncio import start_server
import time

print("Ingrese cualquier tipo de cadena del formato: (a|b)*abb")
string = str(input("Ingrese cadena: "))


def transition_process(string):
    state = 0
    # inicializo el estado en 0
    print(f"Ha introducido: '{string}'")
    print("INICIANDO AUTOMATA...")
    # recorro la cadena de entrada con un for
    for i in range(len(string)):
        # igualo la cadena de la posicion actual a la transicion
        transition = string[i]
        #Para el Estado A
        if state == 0:       
       
            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue

            elif transition == 'b':
                print("ESTADO: ", state)
                state = 2
                time.sleep(1)
                continue

            else:
                print("ERROR")
                state=0
                return
                 
        #Para el Estado B
        if state == 1:   

            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue

            elif transition == 'b':
                print("ESTADO: ", state)
                state = 3  
                time.sleep(1)           
                continue

            else:
                print("ERROR")
                state=0
                return
        
        #Para el Estado C
        if state == 2:

            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue

            elif transition == 'b':
                print("ESTADO: ", state)
                state = 2
                time.sleep(1)              
                continue

            else:
                print("ERROR")
                state=0
                return

        #Para el Estado D
        if state == 3:

            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue

            elif transition == 'b':
                print("ESTADO: ", state)
                state = 4
                time.sleep(1)              
                continue
# break: rompe iteracion. #return:rompe funcion. #continue:en una iteracion (for-while) lee el siguiente valor.
            else:
                print("ERROR")
                state=0
                return
        
        #Para el Estado E
        if state == 4:

            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue

            elif transition == 'b':
                print("ESTADO: ", state)
                state = 2
                time.sleep(1)              
                continue

            else:
                print("ERROR")
                state=0
                return
    end_state(state)


def end_state(state):
    if state == 4:
        print('Estado de Finalizacion Correcto!. Estado: ', state)
    else:
        print('Estado de Finalizacion INCORRECTO!. Estado: ', state)

transition_process(string)


next = "Siguiente estado..."
end_msg = "Estado final alcanzado"
error_msg = "Estado incorrecto"
input_msg = "Ingrese entrada: "
input_msg_2 = "Ingrese caracter: "

def main(entrada):
    lista = list(entrada)
    print('Estado 1:', lista[0])
    print(next)
    print('Estado 1:', lista[1])
    print(next)
    print('Estado 1:', lista[2])
    print(next)
    print('Estado 1:', lista[3])

# def automata(entrada):
    #lista = list(entrada)
    #for i in range(len(lista[0])):
     #   caracter = input(input_msg_2)
      #  if lista[i] ==  caracter:
       #     print(next)
        #    i += 1
       # else:
        #    print(error_msg)
   # if i == len(lista[-1]):
    #    print(end_msg)

# entrada = input(input_msg)
if __name__ == '__main__':
    entrada = input(input_msg)
    main(entrada)

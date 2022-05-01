import re

def main():
    input_1 = input("Seleccione el dato a analizar: ")
    if input_1 == 'a':
        use_email()
    elif input_1 == 'b':
        use_url()
    elif input_1 == 'c':
        use_ipv4()
    elif input_1 == 'd':
        use_password()
    else:
        print("error")

def use_email():
    fs = open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "w+")
    for i in range(0, 2):
        string = input("ingrese url: ")
        with open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "a") as fs:
            fs.write(str(string))
            fs.write("\n")
            fs.close()
    fs = open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "r")
    lines = fs.readlines()

    # declaro regex
    regex = re.compile('''(^(https|http)\:\/\/?|(www\.)?)(([a-zA-Z0-9])+|([-_]))(\.)(net|com|org|onion)([\.])?(ar|edu)?$''')
    
    # creo listas
    valid = []
    invalid = []

    # uso un for para recorrer las lineas del archivo
    for line in lines:
        line = line.rstrip()
        result = regex.search(line)
        # busco en la regex el patron indicado y agrego a la lista si es valido
        if result:
            valid.append(line)    
        else:
            invalid.append(line)
    # printeo los resultados
    print("Emails VALIDOS")
    print(valid)
    print("Emails INVALIDOS")
    print(invalid)

def use_url():
    fs = open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "w+")
    for i in range(0, 2):
        string = input("ingrese url: ")
        with open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "a") as fs:
            fs.write(str(string))
            fs.write("\n")
            fs.close()
    fs = open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "r")
    lines = fs.readlines()

    # declaro regex
    regex = re.compile('''(^(https|http)\:\/\/?|(www\.)?)(([a-zA-Z0-9])+|([-_]))(\.)(net|com|org|onion)([\.])?(ar|edu)?$''')
    
    # creo listas
    valid = []
    invalid = []

    # uso un for para recorrer las lineas del archivo
    for line in lines:
        line = line.rstrip()
        result = regex.search(line)
        # busco en la regex el patron indicado y agrego a la lista si es valido
        if result:
            valid.append(line)    
        else:
            invalid.append(line)
    # printeo los resultados
    print("URLs VALIDAS")
    print(valid)
    print("URLs INVALIDAS")
    print(invalid)


def use_ipv4():
    fs = open("/home/aaron/Documents/Facultad/Tercer_Año/Automatas_y_Gramatica/Automatas/TP_4/ipv4.txt", "w+")
    for i in range(0, 4):
        string = input("ingrese direccion ipv4: ")
        with open("/home/aaron/Documents/Facultad/Tercer_Año/Automatas_y_Gramatica/Automatas/TP_4/ipv4.txt", "a") as fs:
            fs.write(str(string))
            # fs.write(str(string[i]))
            fs.write("\n")
            fs.close()
    fs = open("/home/aaron/Documents/Facultad/Tercer_Año/Automatas_y_Gramatica/Automatas/TP_4/ipv4.txt", "r")
        # with open("/home/aaron/Documents/Automatas/Automatas/TP_4/ipv4.txt", "r") as fs:
    lines = fs.readlines()

    ip_ranges = re.compile('''^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$''')

    valid = []
    invalid = []

    for line in lines:
        line = line.rstrip()
        result = ip_ranges.search(line)
        if result:
            valid.append(line)    
        else:
            invalid.append(line)
    print("IPs VALIDAS")
    print(valid)
    print("IPs INVALIDAS")
    print(invalid)



def use_password():
    fs = open("/home/aaron/Documents/Facultad/Tercer_Año/Automatas_y_Gramatica/Automatas/TP_4/passw.txt", "w+")
    for i in range(0, 2):
        string = input("ingrese su contraseña: ")
        with open("/home/aaron/Documents/Facultad/Tercer_Año/Automatas_y_Gramatica/Automatas/TP_4/passw.txt", "a") as fs:
            fs.write(str(string))
            # fs.write(str(string[i]))
            fs.write("\n")
            fs.close()
    fs = open("/home/aaron/Documents/Facultad/Tercer_Año/Automatas_y_Gramatica/Automatas/TP_4/passw.txt", "r")
        # with open("/home/aaron/Documents/Automatas/Automatas/TP_4/ipv4.txt", "r") as fs:
    lines = fs.readlines()

#Buscar una letra MAY
#Buscar letra MIN
#Buscar 1 numero
#Buscar 1 simbolo (def 5)
#LEN MIN de 8 car

    passw_range = re.compile('''^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%?&]).{8,20}$''')

    valid = []
    invalid = []

    for line in lines:
        line = line.rstrip()
        result = passw_range.search(line)
        if result:
            valid.append(line)    
        else:
            invalid.append(line)
    print("PASSWs VALIDAS")
    print(valid)
    print("PASSWs INVALIDAS")
    print(invalid)

if __name__ == '__main__':
    main()


#Trabajo Practico N1 - REGEX
#Alumnos: Santiago Zapata, Nicolas Mayoral, Aaron Moya


import time
import re

def main():
    print('''
    OPCIONES:

    a) Email
    b) Direccion URL
    c) Direccion IPV4
    d) Contraseña segura
    e) Salir
    ''')
    input_1 = input("Seleccione el dato a analizar: ")
    print("\n")
    if input_1 == 'a':
        use_email()
    elif input_1 == 'b':
        use_url()
    elif input_1 == 'c':
        use_ipv4()
    elif input_1 == 'd':
        use_password()
    elif input_1 == 'e':
        print("Saliendo del sistema...")
        exit()
    else:
        print("error")

# Funcion para Validacion de EMAIL
def use_email():
    fs = open(r"E:\Proyectos python\Automatas\TP_4\emails.txt", "r")
    lines = fs.readlines()

    # declaro regex
    regex = re.compile('''(([a-zA-Z0-9_-])+(\@)(hotmail|gmail|yahoo|outlook|um)(\.)(es|com|edu|us)([\.])?(ar|uk)?$)''')
    
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
    print("Emails VALIDOS:\n")
    print(valid, "\n")
    print("Emails INVALIDOS:\n")
    print(invalid, "\n")
    return_menu()


# Funcion para Validacion de URL
def use_url():
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
    print("URLs VALIDAS:\n")
    print(valid, "\n")
    print("URLs INVALIDAS:\n")
    print(invalid, "\n")
    return_menu()

# Funcion para Validacion de IPV4
def use_ipv4():
    fs = open("E:\Proyectos python\Automatas\TP_4\ipv4.txt", "r")
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
    print("IPs VALIDAS:\n")
    print(valid, "\n")
    print("IPs INVALIDAS:\n")
    print(invalid, "\n")
    return_menu()


# Funcion para Validacion de CONSTRASEÑAS
def use_password():
    print('''
    Su contraseña debe contener los siguientes parametros: ''')
    print('''
    - Debe contener una mayuscula
    - Debe contener una minuscula
    - Debe contener al menos un caracter especial: % & @ ? !
    - Debe contener al menos un numero
    - Debe ser minimo 8 caracteres
    ''')
    fs = open("E:\Proyectos python\Automatas\TP_4\passw.txt", "r")
    lines = fs.readlines()

    passw_range = re.compile('''^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%?&!]).{8,20}$''')

    valid = []
    invalid = []

    for line in lines:
        line = line.rstrip()
        result = passw_range.search(line)
        if result:
            valid.append(line)    
        else:
            invalid.append(line)
    print("PASSWs VALIDAS:\n")
    print(valid, "\n")
    print("PASSWs INVALIDAS:\n")
    print(invalid, "\n")
    return_menu()

def return_menu():
    input_2 = input("Quiere volver al menu principal? (si/no) ")
    print("\n")
    if input_2 == 'si':
        print("Regresando...")
        time.sleep(1)
        main()
    else:
        exit()

if __name__ == '__main__':
    main()


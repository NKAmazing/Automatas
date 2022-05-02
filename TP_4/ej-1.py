#Trabajo Practico N1 - REGEX
#Alumnos: Santiago Zapata, Nicolas Mayoral, Aaron Moya


import re

def main():
    print('''
    OPCIONES:
    a) Email
    b) Direccion URL
    c) Direccion IPV4
    d) Contraseña segura
    ''')
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

# Funcion para Validacion de EMAIL
def use_email():
    fs = open(r"E:\Proyectos python\Automatas\TP_4\emails.txt", "w+")
    for i in range(0, 5):
        string = input("\ningrese email: ")
        with open(r"E:\Proyectos python\Automatas\TP_4\emails.txt", "a") as fs:
            fs.write(str(string))
            fs.write("\n")
            fs.close()
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
    print("Emails VALIDOS")
    print(valid)
    print("Emails INVALIDOS")
    print(invalid)


# Funcion para Validacion de URL
def use_url():
    fs = open(r"E:\Proyectos python\Automatas\TP_4\url.txt", "w+")
    for i in range(0, 5):
        string = input("\ningrese url: ")
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

# Funcion para Validacion de IPV4
def use_ipv4():
    fs = open("E:\Proyectos python\Automatas\TP_4\ipv4.txt", "w+")
    for i in range(0, 5):
        string = input("\ningrese direccion ipv4: ")
        with open("E:\Proyectos python\Automatas\TP_4\ipv4.txt", "a") as fs:
            fs.write(str(string))
            fs.write("\n")
            fs.close()
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
    print("IPs VALIDAS")
    print(valid)
    print("IPs INVALIDAS")
    print(invalid)


# Funcion para Validacion de CONSTRASEÑAS
def use_password():
    fs = open("E:\Proyectos python\Automatas\TP_4\passw.txt", "w+")
    print('''
    Su contraseña debe contener los siguientes parametros: ''')
    print('''
    - Debe contener una mayuscula
    - Debe contener una minuscula
    - Debe contener al menos un caracter especial: % & @ ? !
    - Debe contener al menos un numero
    - Debe ser minimo 8 caracteres
    ''')
    for i in range(0, 5):
        string = input("ingrese su contraseña: ")
        with open("E:\Proyectos python\Automatas\TP_4\passw.txt", "a") as fs:
            fs.write(str(string))
            fs.write("\n")
            fs.close()
    fs = open("E:\Proyectos python\Automatas\TP_4\passw.txt", "r")
    lines = fs.readlines()

# Buscar una letra MAY
# Buscar letra MIN
# Buscar 1 numero
# Buscar 1 simbolo (def 5)
# LEN MIN de 8 car#

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
    print("PASSWs VALIDAS")
    print(valid)
    print("PASSWs INVALIDAS")
    print(invalid)

if __name__ == '__main__':
    main()


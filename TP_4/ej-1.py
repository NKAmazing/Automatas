import re
from unittest import result

def main():
    input_1 = input("Seleccione el dato a analizar: ")
    if input_1 == 'a':
        use_email()
    elif input_1 == 'b':
        use_url()
    elif input_1 == 'c':
        use_ipv4()
    else:
        print("error")

def use_email():
    fd = open("E:\Proyectos python\Automatas\TP 4\emails.txt", "w+")
    for i in range(0, 4):
        string = input("ingrese email: ")
        with open("E:\Proyectos python\Automatas\TP 4\emails.txt", "a") as fd:
            fd.write(str(string[i]))
            fd.write("\n")
    fd = open("E:\Proyectos python\Automatas\TP 4\emails.txt", "r")
    lines = fd.readlines()
    # print(lines)

    patron = '[a-z A-Z]'
    patron_2 = '[a-z A-Z 0-9 _ . - yahoo gmail hotmail um outlook fr uk de be es]'
    patron_domain = '[yahoo gmail hotmail um outlook]'
    patron_country = '[fr uk de be es]'

    for i in range(len(lines)):
        if re.search(patron_2, lines[i]):
            print("email correcto")
        else:
            print("error")

def use_url():
    fs = open(r"E:\Proyectos python\Automatas\TP 4\url.txt", "w+")
    for i in range(0, 4):
        string = input("ingrese url: ")
        with open(r"E:\Proyectos python\Automatas\TP 4\url.txt", "a") as fs:
            fs.write(str(string[i]))
            fs.write("\n")
    fs = open(r"E:\Proyectos python\Automatas\TP 4\url.txt", "r")
    lines = fs.readlines()
    # print(lines)

    patron = '[a-z A-Z . 0-9]'
    patron_opt = '[http https www : /]'
    

    for i in range(len(lines)):
        if re.search(patron, lines[i]):
            if re.search(patron_opt, lines[i]):
                print("url correcto con protocolo incluido")
            else:
                print("url correcto")
        else:
            print("error en la url")
    

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

    ip_ranges = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')

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

#([0-2][0-5][0-5])
    # [0-9]|[0-9]{2}|[0-2][0-5][0-9]
    #asdhsad

if __name__ == '__main__':
    main()




# if re.search(patron, lines[0]):
    #     print("el email es correcto")
    # elif re.search(patron_2, lines[0]):
    #     print("el email es correcto")
    # elif re.search(patron_domain, lines[0]):
    #     print("el email es correcto")
    # elif re.search(patron_country, lines[0]):
    #     print("el email es correcto")
    # else:
    #     print("el email no corresponde con la sintaxis")
    # if re.search(patron, lines[0]) and re.search(patron_2, lines[0]) and re.search(patron_domain, lines[0]) and re.search(patron_country, lines[0]):
    #     print("el email es correcto")
    # else:
    #     print("el email no corresponde con la sintaxis")
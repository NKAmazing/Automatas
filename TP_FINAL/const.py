# Constants

# REGEX
DATETIME_REGEX = ('''(0[1-9]|[12]\d|3[01])\/([1-9]|1[0-2])\/[12]\d{3}  ([01][0-9]|2[0-3]):[0-5]\d:[0-5]\d''')

# paths
PATH = "E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\libros.txt"
PATH_1 = "E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\ejemplo_2.txt"

# paths con raw incluido (un solo backslash '\' )
PATH_2 = r"E:\Proyectos python\Computacion 1 FINAL\FINAL 16-05-22\N_Ejercicio\archives\ejemplo.txt"
PATH_3 = r"E:\Proyectos python\Computacion 1 FINAL\FINAL 16-05-22\N_Ejercicio\archives\ejemplo_2.txt"
# paths con format incluido
file_name = "ejemplo"
file_name_2 = "ejemplo_2"
PATH_4 = f"E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\archives\\{file_name}.txt"
PATH_5 = f"E:\\Proyectos python\\Computacion 1 FINAL\\FINAL 16-05-22\\N_Ejercicio\\archives\\{file_name_2}.txt"

# paths para usar con Pandas
PATH_CSV = "Usuarios WiFi.csv"
PATH_XLSX = "Usuarios WiFi.xlsx"
FULLPATH_XLSX = r"C:\Users\Nicolas\Proyectos Programacion\Automatas\TP_FINAL\Usuarios WiFi.xlsx"
PATH_XLSX_USER = "Usuarios.xlsx"
PATH_XLSX_MACS = "MACs de Usuario.xlsx"
PATH_DATE_USR = "Conexiones de usuario.xlsx"
PATH_TRAFFIC_USR = "Trafico de Usuario.xlsx"
PATH_MAC_USER = "Cantidad de Veces de una MAC.xlsx"

# inputs
QUESTION_RET = "Do yo want to return to Main Menu? (Y/N) "
INP_SHOW_DATA = "Do you wish to view the full information of the Connections? (Y/N) "
INP_A = "From what asignature do you want to check students? "
INP_Q = "What queue do you want to attend? 1/2 : "
INP_DB = "What queue do you want to add to database? 1/2 : "
NAME = "Enter name: "
LASTNAME = "Enter lastname: "
ID_NUMBER = "Enter ID Number: "
AUTHOR = "Enter Author: "
ISB = "Enter ISB: "
COUNTRY = "Enter country: "
AGE = "Enter Age: "
QUESTION_SL = "What list do you want to see? bk/cl : "
UN_INP = "Enter Username: "
DATETIME_INPUT = "Enter the date time with this format (DD/MM/YYYY): "
DATETIME_INPUT_1 = "Enter the first date time with this format (DD/MM/YYYY) : "
DATETIME_INPUT_2 = "Enter the second date time with this format (DD/MM/YYYY) : "
DATETIME_RANGE_INPUT = "Do you want to use a range to search? (Y/N) "
MAC_USER_INP = "Enter MAC of the User to analyze: "

# errores o emptys
ERR = "UNEXPECTED ERROR"
EMPTY_Q = "This list is empty. No book to add to file."
EMPTY_Q_2 = "This queue is empty. No client to add to Database."
EMPTY_T = "This list of clients treated is empty."
EMPTY_LIST = "This list is empty. No book to add."
EMPTY_LR = "This list is empty. No book to delete."
EMPTY_LR2 = "This list is empty. No client to delete."
EMPTY_CL = "This list is empty. No client to add."
OUT_RANGE = "The object you selected is not in the list."
WRONG_LIST = "ERROR. The option you selected is not a list."
EMPTY_DICT = "This assigned book list is empty."
NO_MATCH = "There's no match for the data you are searching."

# menu
MENU = '''
CONNECTION REPORTING SOFTWARE SERVICE

OPTIONS:

    a) List all sessions of a User through the ID.
    b) List all logins in a specific time.
    c) Total time of session of a user.
    d) Check MAC from a User.
    e) List all of the differents MAC of a User.
    f) List all Users connected to an AP.
    g) Show traffic of a User.
    i) List APs sorted by total traffic

    h) Help.

    q) Quit.

What do you wish to do?

'''
# help
HELP = '''
HELP:

This is a connection reporting software. You can check 
or view the information of multiples connections about 
different users.

Here you will find the instructions:

- Press the correct Key for option you want.
- Enter the data the software is going to need.
- View the information that the software provides you.
- After choose an option you can return to the main menu if you wish so.
- To exit the program, you have to press the correct option key (q) in the terminal.

'''

# mensajes
RETURN_MENU = "Returning to Main Menu..."
SEARCHING_DATA = "Looking for any matches..."
LOADING_DATA = "Loading data..."
LOAD_DATA = "The data was successfully loaded."
CLIENT_ADDED = "The client was successfully added."
DEL_DATA = "The data has been deleted successfully from file."
CLIENT_ATTENDED = "All clients was successfully attended."
USER_NOT_FOUND = "The user was not found."
MAC_NOT_FOUND = "The MAC was not found."
WRONG_DT = "The value you entered is not in the format datetime."
WRONG_DT_2 = "The second value you entered is not in the format datetime."
INSC_FALSE = "You cannot inscribed to this assignature."
INSC_TRUE = "You have successfully inscribed to the assignature."
NOT_INT_DNI = "Need to be a int digit!"
LEN_DNI = "Need to be a real Document!"
DNI_TRUE = "This DNI has validated successfully."
BOOK_DEL = "The book has been deleted from cataloge."
CHOOSE_BOOK = "Choose a Book from book list: "
CHOOSE_CLIENT = "Choose a Client from client list: "
BK_ASSIGNED = "The book was assigned to a client."
INP_FB = "You have chosen option: "
INFO_HELP = "To test how it works."
VALIDATE_CHECKING = "Validating data..."
VALIDATE_CORRECT = "The data was validated successfully!"
DT_RANGE_MSG = "You need to set a Datetime range below."

# operaciones de string
JUMP_LINE = "\n"

# mensajes de salida
EXIT = "Exiting the program..."
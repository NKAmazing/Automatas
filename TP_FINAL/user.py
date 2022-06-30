from operator import contains
import re
import const as cs
import time
import pandas as pd
from datetime import datetime
class User:

    def operate_xlsx_file(self):
        df = pd.read_excel(cs.PATH_XLSX) # lee el archivo
        df = df.dropna()
        return df

    def list_session_id(self):
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP) # ingresa el usuario
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file() # llama a la funcion
        if inp in df.values:
            # separa estas dos columnas con loc
            df_loc = df.loc[:,["ID Conexion unico", "Usuario"]]
            # busca un usuario en esa columna y lo separa con loc
            usuarios = df_loc[df_loc["Usuario"].str.contains(inp)]
            print(cs.JUMP_LINE)
            print(usuarios)
            usuarios.to_excel(cs.PATH_XLSX_USER) # guarda los datos en un excel
        else:
            print(cs.USER_NOT_FOUND)
        time.sleep(0.5)

    def print_xlsx(self):
        df = self.operate_xlsx_file()
        print(df)

    def list_macs_user(self):
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        if inp in df.values:
            df_loc = df.loc[:,["MAC Cliente", "Usuario"]]
            usuarios = df_loc[df_loc["Usuario"].str.contains(inp)]
            print(cs.JUMP_LINE)
            print(usuarios)
            usuarios.to_excel(cs.PATH_XLSX_MACS)
        else:
            print(cs.USER_NOT_FOUND)
        time.sleep(0.5)
    #desde acá estoy agregando cosas
    def datetime_search(self):
        print(cs.JUMP_LINE)
        regex = re.compile('''(0[1-9]|[12]\d|3[01])-([1-9]|1[0-2])-[12]\d{3} ([01][0-9]|2[0-3]):[0-5]\d:[0-5]\d''')
        inp = str(input(cs.DATETIME_INPUT))
        result = regex.fullmatch(inp)

        if result:
            usr_input = input(cs.UN_INP)
            opt_input = str(input(cs.DATETIME_RANGE_INPUT))
            df = self.operate_xlsx_file()
            df_loc = df.loc[:, ["Inicio de Conexi¢n", "Fin de Conexio", "Usuario"]]
            # fecha_1 = datetime.strptime(inp, '%d/%m/%Y')
            # fecha_1 = fecha_1.strftime("%d-%m-%Y")
            # print(type(fecha_1))
            if opt_input == "y" or opt_input == "Y":
                inp_2 = input(cs.DATETIME_INPUT)
                fecha_2 = datetime.strptime(inp_2, '%d/%m/%Y')
            else:
                print(cs.SEARCHING_DATA)
                fecha_usr = df_loc[(df_loc["Usuario"].str.contains(usr_input))]
                resultado = fecha_usr.loc[df["Inicio de Conexi¢n"].astype(str).isin([inp])]
                print(cs.JUMP_LINE)
                print(resultado)
                resultado.to_excel(cs.PATH_DATE_USR)
        else:
            print(cs.ERR)
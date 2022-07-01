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

    def mac_user_devices(self):
        print(cs.JUMP_LINE)
        inp = input(cs.MAC_USER_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        if inp in df.values:
            df_loc = df.loc[:,["MAC Cliente", "Usuario"]]
            macs = df_loc[df_loc["MAC Cliente"].isin([inp])]
            mac_user = macs.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Cantidad de Veces Utilizada')
            print(cs.JUMP_LINE)
            print(mac_user)
            mac_user.to_excel(cs.PATH_MAC_USER)
        else:
            print(cs.JUMP_LINE)
            print(cs.MAC_NOT_FOUND)
        time.sleep(0.5)

    # desde acá estoy agregando cosas
    def datetime_search(self):
        print(cs.JUMP_LINE)
        # regex datetime
        regex = re.compile(cs.DATETIME_REGEX)
        print(cs.DT_RANGE_MSG)
        time.sleep(2)
        print(cs.JUMP_LINE)
        date_1 = str(input(cs.DATETIME_INPUT_1)) # ingreso primera fecha
        validation_date = regex.fullmatch(date_1) # valido con fullmatch
        print(cs.JUMP_LINE)
        print(cs.VALIDATE_CHECKING)
        time.sleep(2)
        if validation_date: # validacion correcta
            print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
            date_2 = str(input(cs.DATETIME_INPUT_2)) # ingreso segunda fecha
            validation_date_2 = regex.fullmatch(date_2) # valido con fullmatch
            print(cs.JUMP_LINE)
            print(cs.VALIDATE_CHECKING)
            time.sleep(2)
            if validation_date_2: # segunda validacion correcta
                print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                usr_input = input(cs.UN_INP) # ingreso usuario
                print(cs.JUMP_LINE, cs.SEARCHING_DATA)
                df = self.operate_xlsx_file() # llamo a la funcion para leer el archivo
                if usr_input in df.values and date_1 < date_2: # verifico si existe el usuario y si el rango de fechas es correcto
                    df_loc = df.loc[: , ["Usuario","Inicio de Conexi¢n"]] # separo estas dos columnas con loc
                    usr_df = df_loc[df_loc["Usuario"].isin([usr_input])] # busco mi usuario ingresado
                    date_df = usr_df.loc[df["Inicio de Conexi¢n"].between(date_1, date_2)] # busco entre mi rango de fechas
                    print(cs.JUMP_LINE)
                    print(date_df)
                    date_df.to_excel(cs.PATH_DATE_USR)
                else: # no match
                    print(cs.JUMP_LINE, cs.NO_MATCH)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_2)
        else:
            print(cs.JUMP_LINE, cs.WRONG_DT)
        time.sleep(0.5)
        

    def traffic_user(self):
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP) # ingresa el usuario
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file() # llama a la funcion
        if inp in df.values:
            # separa estas tres columnas con loc
            df_loc = df.loc[:,["Usuario", "Input Octects", "Output Octects"]]
            # busca un usuario en esa columna y lo separa con loc
            usuarios = df_loc[df_loc["Usuario"].str.contains(inp)]
            print(cs.JUMP_LINE)
            print(usuarios)
            usuarios.to_excel(cs.PATH_TRAFFIC_USR) # guarda los datos en un excel
        else:
            print(cs.USER_NOT_FOUND)
        time.sleep(0.5)
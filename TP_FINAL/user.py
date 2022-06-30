import const as cs
import time
import pandas as pd

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

    def print_csv(self):
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
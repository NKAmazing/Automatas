import const as cs
import time
import pandas as pd

class User:

    def operate_xlsx_file(self):
        df = pd.read_excel("Usuarios WiFi.xlsx")
        df = df.dropna()
        return df

    def list_session_id(self):
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        if inp in df.values:
            df_loc = df.loc[:,["ID Conexion unico", "Usuario"]]
            usuarios = df_loc[df_loc["Usuario"].str.contains(inp)]
            print(cs.JUMP_LINE)
            print(usuarios)
            usuarios.to_excel("Usuarios.xlsx")
        else:
            print(cs.USER_NOT_FOUND)

    def print_csv(self):
        # data = pd.read_csv(cs.PATH_CSV, header=0)
        # print(data.shape)
        # print(data.head(10))
        df = self.operate_csv_file()
        print(df)

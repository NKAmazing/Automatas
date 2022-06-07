import const as cs
import time
import pandas as pd

class User:

    def operate_csv_file(self):
        data = pd.read_csv(cs.PATH_CSV)
        df = pd.DataFrame(data) 
        return df

    def list_session_id(self):
        print(cs.JUMP_LINE)
        df = self.operate_csv_file()
        inp = input(cs.UN_INP)
        if inp in df.values:
            df2 = df.loc["ID Conexion unico", "Usuario"]
            # revisar esto para poder listar con loc
        print("Aca voy a listar lo del ejercicio a)")
        time.sleep(1)
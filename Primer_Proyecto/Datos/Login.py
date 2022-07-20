import pypyodbc as odbc
import sys
sys.path.append(r'C:\Users\sebas\Desktop\Jupyter\Primer_Proyecto')
from Datos.StringConexion import String_Conexion
class login():
    def get_data(user):
        conn = odbc.connect(String_Conexion.string())
        cursor = conn.cursor()
        cursor.execute(f"select * from users where userID={user}")
        data=cursor.fetchall()
        conn.close()
        return data

import sys
sys.path.append(r'C:\Users\sebas\Desktop\Jupyter\Primer_Proyecto')
from Datos.Login import login as D
class login():
    def trylog(usuario,password):
        data = D.get_data(usuario)
        if(usuario==data[0][0] and password==data[0][2]):
            return True
        else:
            return False
            

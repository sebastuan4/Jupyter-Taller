from lib2to3.pgen2.driver import Driver
from multiprocessing import connection
from grpc import server
import pypyodbc as odbc

driverName = "SQL Server"
serverName ="SEBASTUA4\SQLEXPRESS"
databaseName ='primeraBase'
#Driver={SQL Server};Server=myServerAddress;Database=myDataBase;Trusted_Connection=Yes;
#Creamos el string de conexion como tenemos arriba
connection_string = f"DRIVER={driverName}; SERVER={serverName}; DATABASE={databaseName}; Trust_Connection=yes;"
conn = odbc.connect(connection_string)
print(conn)#Comprobamos que la conexion funciona


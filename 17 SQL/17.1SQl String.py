
import pypyodbc as odbc
driverName = "SQL Server"
myServerAddress ="SEBASTUA4\SQLEXPRESS"
databaseName ='primeraBase'
myUsername="clase"
myPassword="clase"
#Creamos el string de conexion como tenemos arriba
connection_string = f"Driver={driverName};Server={myServerAddress},1433;Database={databaseName};User Id={myUsername};Password={myPassword};"
conn = odbc.connect(connection_string)
print(conn)#Comprobamos que la conexion funciona



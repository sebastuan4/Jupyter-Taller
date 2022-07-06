import pypyodbc as odbc
driverName = "MySQL ODBC 8.0 ANSI Driver"
serverName ="127.0.0.1"
databaseName ='primeraBase'
username="root"
password="DeathN0te"
#Driver={SQL Server};Server=myServerAddress;Database=myDataBase;Trusted_Connection=Yes;
#Creamos el string de conexion como tenemos arriba
connection_string=f'DRIVER={driverName};SERVER={serverName};DATABASE={databaseName};UID={username};PWD={password}'
conn = odbc.connect(connection_string)
print(conn)#Comprobamos que la conexion funciona


import pypyodbc as odbc
driverName = "MySQL ODBC 8.0 ANSI Driver"
serverAddres ="127.0.0.1"
databaseName ='primerabase'
username="root"
password="DeathN0te"
connection_string=f'DRIVER={driverName};SERVER={serverAddres};DATABASE={databaseName};UID={username};PWD={password}'
conn = odbc.connect(connection_string)
#Creamos un cursor para interactuar con la base de datos
cursor = conn.cursor()
#nombre=input("Ingrese nombre")
cursor.execute(f"select * from primeraTable")

#Forma 1----------------------------------------------------------------------------------------
#Traemos los datos del query uno por uno
data=cursor.fetchone()
print(data)
#Creamos un bucle para traer todos los datos
while data:
    print(data)
    data=cursor.fetchone()

#Forma 2----------------------------------------------------------------------------------------
#Traemos todos los datos
data = cursor.fetchall()
#Creamos un bucle para ver
for datos in data:
    print(datos)

#Cerramos la conexion
conn.close()


import pypyodbc as odbc

driverName = "SQL Server"
serverName ="SEBASTUA4\SQLEXPRESS"
databaseName ='primeraBase'
#Driver={SQL Server};Server=myServerAddress;Database=myDataBase;Trusted_Connection=Yes;
#Creamos el string de conexion como tenemos arriba
connection_string = f"DRIVER={driverName}; SERVER={serverName}; DATABASE={databaseName}; Trust_Connection=yes;"
conn = odbc.connect(connection_string)
#Creamos un cursor para interactuar con la base de datos
cursor = conn.cursor()
nombre=input("Ingrese nombre")
cursor.execute(f"select * from primeraTabla where nombre='{nombre}'")

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


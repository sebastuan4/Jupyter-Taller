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
#CRUD Create,Read,Update,Delete
#Create/Insert
nombre=input("nombre")
profesion=input("profesion")
query=f"""
    insert primeraTabla(nombre,profesion)
    values('{nombre}','{profesion}')
"""
cursor.execute(query)
#Read
query="""
    select * from primeraTabla
"""
cursor.execute(query)
#Update
nombre=input("nombre")
id=input("id")
query=f"""
    update primeraTabla set nombre={nombre} where id={id}
"""
cursor.execute(query)
#Delete
id=input("id")
query=f"""
    delete from primeraTabla where id={id}
"""
cursor.execute(query)

#Traemos todos los datos
data = cursor.fetchall()
#Creamos un bucle para ver
for datos in data:
    print(datos)

#Cerramos la conexion
conn.close()


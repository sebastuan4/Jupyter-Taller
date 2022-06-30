class String_Conexion():
    def string():
        driverName = "SQL Server"
        serverName ="SEBASTUA4\SQLEXPRESS"
        databaseName ='primeraBase'
        connection_string = f"DRIVER={driverName}; SERVER={serverName}; DATABASE={databaseName}; Trust_Connection=yes;"
        return connection_string

class String_Conexion():
    def string():
        __driverName = "SQL Server"
        __serverName ="SEBASTUA4\SQLEXPRESS"
        __databaseName ='logear'
        __connection_string = f"DRIVER={__driverName}; SERVER={__serverName}; DATABASE={__databaseName}; Trust_Connection=yes;"
        return __connection_string

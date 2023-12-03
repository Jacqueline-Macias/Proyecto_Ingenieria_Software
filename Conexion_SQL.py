import mysql.connector

class connect_foodsoft:
    def __init__(self, Host, username, PassWord, Port, database_name):
        self.connection = mysql.connector.connect(host=Host,
                                      user=username,
                                      passwd=PassWord,
                                      port=Port,
                                      database=database_name)
        self.cursor = self.connection.cursor()

class provider(connect_foodsoft):

    def Add(self,id,name,phone,email,type,rfc):
        try:
            sql = "INSERT INTO proveedor(id_proveedor,nombre,telefono,correo,tipo_cadena,rfc) VALUES('{}','{}','{}','{}','{}','{}')".format(id,name,phone,email,type,rfc)
            self.cursor.execute(sql)
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            raise
    
    def modifier(self,id,name,phone,email,type,rfc):
        sql = "UPDATE proveedor SET nombre='{}',telefono='{}',correo='{}',tipo_cadena='{}',rfc='{}' WHERE id_proveedor = '{}'".format(
            name, phone, email, type, rfc,id)
        self.cursor.execute(sql)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
    
    def select_provider(self,id):
        sql = "SELECT * FROM proveedor WHERE id_proveedor = '{}'".format(id)
        self.cursor.execute(sql)
        date = self.cursor.fetchone()
        self.cursor.close()
        self.connection.close()

        return date


        
            




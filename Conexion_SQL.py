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

    def Add(self,id,name,phone,email,typ,rfc):
        try:
            sql = "INSERT INTO proveedor(id_proveedor,nombre,telefono,correo,tipo_cadena,rfc) VALUES('{}','{}','{}','{}','{}','{}')".format(int(id),name,phone,email,typ,rfc)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            self.connection.close()
    
    def modifier(self,id,name,phone,email,typ,rfc):
        try:
            sql = "UPDATE proveedor SET nombre='{}',telefono='{}',correo='{}',tipo_cadena='{}',rfc='{}' WHERE id_proveedor = '{}'".format(
                name, phone, email, typ, rfc,id)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            self.connection.close()
    
    def select_provider(self,id):
        try:
            sql = "SELECT * FROM proveedor WHERE id_proveedor = '{}'".format(id)
            self.cursor.execute(sql)
            date = self.cursor.fetchone()
        except Exception as Ex:
            print(Ex)
        finally:
            self.connection.close()
            return date
    
    def select_all(self):
        try:
            sql = "SELECT * FROM proveedor"
            self.cursor.execute(sql)
            date = self.cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            self.connection.close()
            return date

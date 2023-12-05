import mysql.connector

class connect_foodsoft:
    def __init__(self, Host, username, PassWord, Port, database_name):
        self.connection = mysql.connector.connect(host=Host,
                                      user=username,
                                      passwd=PassWord,
                                      port=Port,
                                      database=database_name)
    
    def Search_id(self,select,table,objec,id):
        try:
            cursor = self.connection.cursor()
            sql = f"SELECT {select} FROM {table} WHERE {objec} = '{id}'"
            cursor.execute(sql)
            date = cursor.fetchone()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date

class provider(connect_foodsoft):

    def Add(self,id,name,phone,email,typ,rfc):
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO proveedor(id_proveedor,nombre,telefono,correo,tipo_cadena,rfc) VALUES('{}','{}','{}','{}','{}','{}')".format(int(id),name,phone,email,typ,rfc)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
    
    def modifier(self,id,name,phone,email,typ,rfc):
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE proveedor SET nombre='{}',telefono='{}',correo='{}',tipo_cadena='{}',rfc='{}' WHERE id_proveedor = '{}'".format(
                name, phone, email, typ, rfc,int(id))
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
    
    def delete(self, id):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM proveedor WHERE id_proveedor = '{}'".format(
                int(id))
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def select(self,search):
        try:
            cursor = self.connection.cursor()
            sql = f"SELECT {search} FROM proveedor"
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            list_date = []
            for count in date:
                list_date.append(count[0])
            return list_date


    def select_all(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM proveedor"
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date


class supply(connect_foodsoft):

    def Add(self, name_provider, name, min, max, price):
        try:
            id = self.Search_id('id_proveedor','proveedor', 'nombre', name_provider)
            cursor = self.connection.cursor()
            sql = "INSERT INTO insumo(nombre, stock_min, stock_max, precio, id_proveedor) VALUES('{}','{}','{}','{}','{}')".format(name,min,max,price,id[0])
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def modifier(self,name_provider,name,min,max,price):
        try:
            id = self.Search_id('id_proveedor','proveedor', 'nombre', name_provider)
            cursor = self.connection.cursor()
            sql = "UPDATE insumo SET stock_min = '{}', stock_max = '{}', precio = '{}', id_proveedor = '{}' WHERE nombre = '{}'".format(min,max,price,id[0],name)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def select_all(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM insumo"
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date

    def delete(self, name):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM insumo WHERE nombre = '{}'".format(name)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

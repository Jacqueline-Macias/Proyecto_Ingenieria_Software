import mysql.connector
from tkinter import messagebox

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
    
    def Search(self,select,table,objec,id):
        try:
            cursor = self.connection.cursor()
            sql = f"SELECT {select} FROM {table} WHERE {objec} = '{id}'"
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

    def Add(self, name_provider,name,number, min, max, price):
        try:
            id = self.Search_id('id_proveedor','proveedor', 'nombre', name_provider)
            cursor = self.connection.cursor()
            sql = "INSERT INTO insumo(nombre,cantidad ,stock_min, stock_max, precio, id_proveedor) VALUES('{}','{}','{}','{}','{}','{}')".format(name,number,min,max,price,id[0])
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def modifier(self,number,name_provider,name,min,max,price):
        try:
            id = self.Search_id('id_proveedor','proveedor', 'nombre', name_provider)
            cursor = self.connection.cursor()
            sql = "UPDATE insumo SET cantidad = '{}', stock_min = '{}', stock_max = '{}', precio = '{}', id_proveedor = '{}' WHERE nombre = '{}'".format(number,min,max,price,id[0],name)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
    
    def modifier_number(self,name,number):
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE insumo SET cantidad = '{}' WHERE nombre = '{}'".format(number, name)
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

    def select(self, search):
        try:
            cursor = self.connection.cursor()
            sql = f"SELECT {search} FROM insumo"
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


class order(connect_foodsoft):

    def select_all(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM icompra"
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date
    
    def select_all_order(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM icomprainsumo"
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date
    
    def add_order(self,provider,employee,date):

        try:
            id = len(self.select_all()) + 1
            cursor = self.connection.cursor()
            sql = "INSERT INTO icompra(id_icompra, id_proveedor, id_empleado, fecha) VALUES('{}','{}','{}','{}')".format(id,provider,employee,date)
            cursor.execute(sql)
            self.connection.commit()
            band = True
        except Exception as Ex:
            messagebox.showerror("Error","ID ingresado invalido")
            band = False
        finally:
            cursor.close()
            return band
    
    def add(self,id_order,product,price,cantidad):
        try:
            id = len(self.select_all_order()) + 1
            cursor = self.connection.cursor()
            sql = "INSERT INTO icomprainsumo(id_icomprainsumo, id_icompra, insumo, precio, cantidad) VALUES('{}','{}','{}','{}','{}')".format(id,id_order,product,price,cantidad)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
    
    def modifier(self,id,product,price, number):
        try:
            cursor = self.connection.cursor()
            sql = "UPDATE icomprainsumo SET precio = '{}', cantidad = '{}' WHERE id_icompra = '{}' AND insumo = '{}'".format(price,number,id,product)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
    
    def delete(self,id,nombre):
        try:
            curso = self.connection.cursor()
            sql = "DELETE FROM icomprainsumo WHERE id_icompra = '{}' AND insumo = '{}'".format(id,nombre)
            curso.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            curso.close()

    def view(self,id):
        try:
            cursor = self.connection.cursor()
            sql = f'SELECT * FROM vista_icomprainsumo WHERE id_icompra = {id}'
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date
    
    def Search_view(self,id,nombre):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM vista_icomprainsumo WHERE id_icompra = '{}' AND nombre = '{}'".format(id,nombre)
            cursor.execute(sql)
            date = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return date

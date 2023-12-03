import mysql.connector

class connect_foodsoft:
    def __init__(self, Host, username, PassWord, Port, database_name):
        Sql = mysql.connector.connect(host=Host,
                                      user=username,
                                      passwd=PassWord,
                                      port=Port,
                                      database=database_name)
        
        




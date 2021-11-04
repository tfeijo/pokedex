import sqlite3

class DataBase:
    def __init__(self, path):     
        self.con = None

        self.path = path
        
        self .cur = None

        self.connect()

    def connect(self):
        try:
            self.con = sqlite3.connect(self.path, check_same_thread=False)
            self.cur = self.con.cursor()
            print("Banco de dados conectado")

        except ValueError:
            print(ValueError)

            print("Erro na conexão do banco de dados")

    def close(self):
        try:
            self.con.close()
            
            print("Banco de dados desconectado")
        
        except ValueError:
            print(ValueError)

            print("Erro ao encerrar conexão com o banco de dados")

    def execute(self, query):
        try:
            self.cur.execute(query)

            return self.cur.fetchall()
        
        except ValueError:
            print(ValueError)
        
            return None
        
    def save(self):
        try:
            self.con.commit()
        
        except ValueError:
            print(ValueError)
        
            print("Erro ao executar commit")

db = DataBase('src\db\db.db')
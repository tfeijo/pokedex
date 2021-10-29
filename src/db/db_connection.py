import sqlite3

class DataBase:
    def __init__(self, path):     
        self.con = None

        self.path = path

        self.connect()

    def connect(self):
        try:
            self.con = sqlite3.connect(self.path, check_same_thread=False)

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
        cur = self.con.cursor()
        cur.execute(query)
        return cur.fetchall()
        
    def save(self):
        try:
            self.con.commit()
        except ValueError:
            print(ValueError)
            print("Erro ao executar commit")

db = DataBase('src\db\db.db')
import mysql.connector


class Conexao

    def connection(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='agenda'
        )
        self.cursor = self.conexao.cursor()

    def create(self, nome, preco, categoria):
        comando = f'INSERT INTO materiais (nome, preco, categoria) VALUES ("{nome}", "{preco}", "{categoria}")'

        self.cursor.execute(comando)
        self.conexao.commit()

        self.cursor.close()
        self.conexao.close()

    def read(self):
        comando = 'SELECT * FROM materiais'

        self.cursor.execute(comando)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)

        self.cursor.close()
        self.conexao.close()

    def update(self, id, nome, preco, categoria):
        comando = f"UPDATE materiais SET nome = '{nome}', preco = '{preco}', categoria = '{categoria}' WHERE id = {id}"

        self.cursor.execute(comando)
        self.conexao.commit()

        self.cursor.close()
        self.conexao.close()

    def delete(self, id):
        comando = f"DELETE FROM materiais WHERE id = '{id}'"

        self.cursor.execute(comando)
        self.conexao.commit()

        self.cursor.close()
        self.conexao.close()
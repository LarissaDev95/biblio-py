from database import Database

class Livro():
    def __init__(self,):
        self.db = Database('livros')

    def create(self,data : dict):
        self.db.insert(data)
        self.db._conn.commit()

    def find_one(self, data):
        return self.db.select().where(data).exec().fetchone()

    def find_all(self, data):
        return self.db.select(data).where().exec().fetchall()

    

livro = Livro()
livro.create({
        'isbn':1234567891234,
            'titulo': 'Star Wars',
            'autor': 'George Lucas',
            'data_lancamento': '1899-02-25',
            'genero_literario': 'Ficção',
            'editora': 'Lucas Filme'
        })
})

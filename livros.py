from database import Database
from livro_orm import LivroORM

class Livros():
    db = Database('livros')

    @classmethod
    def create(cls, data : dict):
        cls.db.insert(data).exec()
        cls.db._conn.commit()

    @classmethod
    def find_one(cls, rules:dict=None):
        return cls.db.select().where(rules).exec().fetchone()
    
    @classmethod
    def find_all(cls, rules:dict=None):
        response = cls.db.select().where(rules).exec().fetchall()
        
        listaLivros = []
        for livro in response:
            listaLivros.append(LivroORM(livro))

        return listaLivros 

    @classmethod
    def update(cls, data=None,*, id):
        return cls.db.update(fields=data, id=id)
    
    @classmethod
    def delete(cls, id:int):
        return cls.db.delete(id)
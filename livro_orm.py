from orm import ORM

class LivroORM(ORM):
    def __init__(self, data: dict):
        super().__init__(data)
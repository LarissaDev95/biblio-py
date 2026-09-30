from orm import ORM

class livroORM(ORM):
    def __init__(self, data: dict):
        super().__init__(data)
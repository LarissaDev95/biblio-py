import mysql.connector

class Database:
    def __init__(self, table : str):
        self.__host__ = "localhost"
        self.__user__ = "root"
        self.__password__ = ""
        self.__database__ = "biblioteca_py"

        self.table = table
        self.query = ""

        self.__initialize__()
        

    def __initialize__(self):
        self._conn = self.__connection__()
        self._cursor = self.__create_cursor__()

    def __connection__(self):
        return mysql.connector.connect(
            host = self.__host__,
            user = self.__user__,
            password = self.__password__,
            database = self.__database__,
        )
    
    def __create_cursor__(self):
        return self._conn.cursor()

    def exec(self):
        self.query +=";"
        print(self.query)
        self._cursor.execute(self.query)
        return self._cursor

    def select(self, fields=["*"]):
        self.query = f"SELECT {self.define_fields(fields)} FROM {self.table} "

        return self

    def define_fields(self, fields):
        campos = ""

        for field in fields:
            campos += f"{field}" if field == fields[-1] else f"{field},"

        return campos

    def where(self, rules:dict= {}):
        self.query += "WHERE "

        for key, value in rules.items():
            self.query+= f"{key} LIKE '%{value}%'"

        return self

def insert(self, fields : dict = {}):
    values = ''
    formated_values = []

    for value in fields.values():
        value
        if isinstance(value, str):
            value = f"'{value}'"

        formated_values.append(str(value))

        values = ",".join(formated_values)
            
        values += f'{value},' if not (value == list(fields.values())[-1]) else f'{value}'

    self.query = f"INSERT INTO {self.table}({','.join(fields)}) VALUES({values})"
    return self


from peewee import *

db = SqliteDatabase('acesso.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique = True)
    senha = CharField()

    class Meta :
        database = db
from peewee import *

db = SqliteDatabase('bank_database.db')

class Usuario(Model):
    nome = CharField()
    telefone = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db

class Conta(Model):
    usuario = CharField()
    saldo = FloatField()
    
    class Meta:
        database = db
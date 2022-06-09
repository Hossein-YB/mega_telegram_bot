from .models import database, Users, Files, Admins


def create_tables():
    with database:
        database.create_tables([Users, Files, Admins])

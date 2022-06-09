from peewee import SqliteDatabase, Model
from peewee import IntegerField, CharField, TextField, ForeignKeyField, BitField

database = SqliteDatabase("bot.db")


class Base(Model):
    class Meta:
        database = database


class Users(Base):
    user_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=300)
    mega_username = CharField(max_length=300)
    maga_password = CharField(max_length=300)

    @classmethod
    def add_user(cls, user_id, username):
        q = cls.insert(user_id=user_id, username=username).on_conflict_ignore(ignore=True)
        q.execute()

    @classmethod
    def admins(cls):
        t = cls.select(Users.user_id).where(Users.is_admin == 1).tuples()
        users = []
        for user_id in t:
            users.append(user_id[0])
        return users


class Admins(Base):
    admin_id = ForeignKeyField(Users, on_delete=True)

    @classmethod
    def add_admin(cls, admin_id):
        cls.replace(user_id=admin_id).execute()


class Files(Base):
    file_id = TextField()
    user_id = ForeignKeyField(Users)
    uploaded = BitField(default=0)
    file_type = CharField(max_length=15)

    @classmethod
    def add_file(cls, file_id, user_id, file_type):
        cls.create(file_id=file_id, user_id=user_id, file_type=file_type)









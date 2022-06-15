from mega import Mega
from mega.errors import RequestError
from utils import Users


class MegaUser:
    def __init__(self, user_id):
        self.mega_user = Mega()
        self.user_info = Users.get_mega_info(user_id)
        self.mega_user = self.mega_user.login(email=self.user_info.mega_username, password=self.user_info.maga_password)

    @classmethod
    def check_user(cls, email, password):
        meg = Mega()
        try:
            meg.login(email, password)
            return True
        except RequestError:
            pass
            return False

    def upload_file(self, file_address):
        path = self.mega_user.find('files')
        if not path:
            self.mega_user.create_folder('files')
            path = self.mega_user.find('files')
        self.mega_user.upload(file_address, path[0])

    def __str__(self):
        info = self.mega_user.get_user()
        if info:
            return {'name': info['name'], 'email': info['email']}
        else:
            return False


if __name__ == "__main__":
    MegaUser.check_user("wpeaj@hi2.in", "psdk@psdk")

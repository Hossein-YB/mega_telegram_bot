from mega import Mega
from utils import Users


class MegaUser:
    def __init__(self, user_id):
        self.mega_user = Mega()
        self.user_info = Users.get_mega_info(user_id)
        self.mega_user = self.mega_user.login(email=self.user_info.mega_username, password=self.user_info.maga_password)

    def upload_file(self, fail_path):
        path = self.mega_user.find_path_descriptor('files')
        if not path:
            self.mega_user.create_folder('files')
        path = self.mega_user.find_path_descriptor('files')
        self.mega_user.upload(fail_path, path[0])

    def __str__(self):
        info = self.mega_user.get_user()
        if info:
            return f"user: {info['name']} email: {info['email']}"
        else:
            return f"user with user ID {self.user_info.user_id} don`t have account in Mega"


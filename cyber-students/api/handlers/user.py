from tornado.web import authenticated
from api.encryption import decrypt_data
from .auth import AuthHandler

class UserHandler(AuthHandler):

    @authenticated
    def get(self):
        self.set_status(200)
        self.response['email'] = decrypt_data(self.current_user['email'])
        self.response['displayName'] = decrypt_data(self.current_user['display_name'])
        self.response['PhoneNumber'] = decrypt_data(self.current_user['PhoneNumber'])
        self.response['Address'] = decrypt_data(self.current_user['Address'])
        self.response['dob'] = decrypt_data(self.current_user['dob'])
        self.response['Disabilities'] = decrypt_data(self.current_user['Disabilities'])
        self.write_json()

from tornado.web import authenticated

from .auth import AuthHandler

class UserHandler(AuthHandler):

    @authenticated
    def get(self):
        self.set_status(200)
        self.response['email'] = self.current_user['email']
        self.response['displayName'] = self.current_user['display_name']
        self.response['PhoneNumber'] = self.current_user['PhoneNumber']
        self.response['Address'] = self.current_user['Address']
        self.response['DateOfBirth'] = self.current_user['DateOfBirth']
        self.response['Disabilities'] = self.current_user['Disabilities']
        self.write_json()

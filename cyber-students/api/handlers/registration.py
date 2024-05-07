from json import dumps
from logging import info
from tornado.escape import json_decode, utf8
from tornado.gen import coroutine

from api.encryption import encrypt_data, encrypt_password

from .base import BaseHandler

class RegistrationHandler(BaseHandler):

    @coroutine
    def post(self):
        try:
            body = json_decode(self.request.body)
            email = body['email'].lower().strip()
            if not isinstance(email, str):
                raise Exception()
            password = body['password']
            if not isinstance(password, str):
                raise Exception()
            display_name = body.get('displayName')
            Address = body.get('Address')
            dob = body.get('dob')
            PhoneNumber = body.get('PhoneNumber')
            Disabilities = body.get('Disabilities')

        except Exception as e:
            self.send_error(400, message='You must enter all the fields, email, name, address, dob, phone number and disability')
            return

        if not email:
            self.send_error(400, message='The email address is invalid!')
            return

        if not password:
            self.send_error(400, message='The password is invalid!')
            return

        if not display_name:
            self.send_error(400, message='The display name is invalid!')
            return
        
        if not Address:
            self.send_error(400, message='The address is invalid!')
            return

        if not dob:
            self.send_error(400, message='The date of birth is invalid!')
            return

        if not PhoneNumber:
            self.send_error(400, message='The phone number is invalid!')
            return 

        if not Disabilities:
            self.send_error(400, message='The disabilities are invalid!')
            return          

        user = yield self.db.users.find_one({
          'email': encrypt_data(email)
        }, {})

        if user is not None:
            self.send_error(409, message='A user with the given email address already exists!')
            return


        yield self.db.users.insert_one({
            'email':encrypt_data(email),
            'password':encrypt_password(password),
            'displayName':encrypt_data(display_name),
            'Address':encrypt_data(Address),
            'dob':encrypt_data(dob),
            'PhoneNumber': encrypt_data(PhoneNumber),
            'Disabilities': encrypt_data(Disabilities)
        })

        self.set_status(200)
        self.response['email'] = email
        self.response['displayName'] = display_name
        self.response['Address'] = Address
        self.response['dob'] = dob
        self.response['PhoneNumber'] = PhoneNumber
        self.response['Disabilities'] = Disabilities

        self.write_json()


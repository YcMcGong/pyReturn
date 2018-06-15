"""
____________________________________________________
 Copyright 2018 Yicong Gong
____________________________________________________
A status response class include an attribute data
status_response.data has the following tags:

[status]: A boolean indicating if the requested-action is successful
[errorMessage]: A message to provide some information about the status
[*data]: User use the attach_data method to insert an object to the *data tag
(*data is an user-defined name)

"""
import json

class status_response():

    def __init__(self):
        self.data = {
            'status': False,
            'errorMessage': []
        }

    def set_status(self, isSuccess):
        self.data['status'] = isSuccess

    def set_errorMessage(self, message):
        self.data['errorMessage'].push(message)

    def attach_data(self, name, data, isSuccess = False):
        self.data[name] = data
        if isSuccess:
            self.data['status'] = True

    def get_response(self):
        return json.dumps(self.data)

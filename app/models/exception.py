from flask import jsonify

# Create custom http error class
class HTTPError(Exception):
    status_code = 400

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message

        if not isinstance(status_code, int):
            raise TypeError('status_code must be an integer')

        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        result = dict(self.payload or {})
        result['message'] = self.message

        return result
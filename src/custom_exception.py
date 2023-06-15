class HttpException(Exception):
    status = None
    message = None

    def __init__(self):
        super().__init__(f'Status code: {self.status}. Message: {self.message}')

class NotFound(HttpException):
    status = 404
    message = 'Resource not found'

class ServerError(HttpException):
    status = 500
    message = 'Internal server error'

# test
raise NotFound()


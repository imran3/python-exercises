class Employee:
    def __init__(self, firstname, lastname):
        self.fullname = f'{firstname} {lastname}'
        self.email = f'{firstname}.{lastname}@mail.com'
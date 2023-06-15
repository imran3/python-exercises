# this class extends the built-int `list` class
class UniqueList(list):

    # add new property to class by overriding constructor
    def __init__(self):
        super().__init__()
        self.someNewProperty = "New property for UniqueList class"
    
    # override the append method to skip adding duplicate items in list
    def append(self, item):
        if item in self:
            return 
        super().append(item)
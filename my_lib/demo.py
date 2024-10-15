
class Demo():

    class_parameter = 'top-level class parameter'
    name = 'Default'

    # Constructor
    def __init__(self):
        self.name = 'Demo'

    # Methods
    def hello_world(self):
        return 'Hello World'

    def hello_lib(self):
        return f'Hello from {self.name}'

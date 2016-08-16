# Functions for str and repr for library
def class_repr(self):
    repr_string = '{} Fields: '.format(self.__name__)
    attributes = vars(self)
    repr_string += ''.join('{}: {} '.format(key, value) for (key, value) in attributes.items())
    return repr_string


def class_string(self):
    return '{}:{}'.format(self.__name__, self.id)

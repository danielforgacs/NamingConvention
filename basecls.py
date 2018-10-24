class Descriptor:
    def __get__(self, instance, cls):
        return instance.__dict__['source']

    def __set__(self, instance, value):
        instance.__dict__['source'] = value


class BaseName:
    source = Descriptor()


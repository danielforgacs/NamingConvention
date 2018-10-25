class Descriptor:
    def __get__(self, instance, cls):
        return instance.__dict__['source']

    def __set__(self, instance, value):
        instance.__dict__['source'] = value


class TypeBase(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, self.typebase):
            raise Exception('==> MUST BE TYPE: '+type(self.typbase))
        super().__set__(instance, value)


class StringType(TypeBase):
    typebase = str

class IntType(TypeBase):
    typebase = int

class SizedString(StringType):
    def __init__(self, lenmin, lenmax):
        self.lenmin = lenmin
        self.lenmax = lenmax

    def __set__(self, instance, value):
        if not self.lenmin <= len(value) <= self.lenmax:
            raise Exception('==> MUST BE LENGTH: ')
        super().__set__(instance, value)


# class TEMP:
#     k = SizedString(lenmin=2, lenmax=3)

# t = TEMP()
# t.k = 1

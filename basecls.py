class Descriptor:
    def __init__(self, attr):
        self.attr = attr

    def __get__(self, instance, cls):
        return instance.__dict__[self.attr]

    def __set__(self, instance, value):
        instance.__dict__[self.attr] = value


class TypeBase(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, self.typebase):
            raise Exception('==> MUST BE TYPE: '+str(self.typebase))
        super().__set__(instance, value)


class StringType(TypeBase):
    typebase = str

class IntType(TypeBase):
    typebase = int

class SizedBase(Descriptor):
    def __init__(self, lenmin, lenmax, **kwargs):
        super().__init__(**kwargs)
        self.lenmin = lenmin
        self.lenmax = lenmax

    def __set__(self, instance, value):
        if not self.lenmin <= len(value) <= self.lenmax:
            raise Exception('==> MUST BE LENGTH: %i - %i' % (self.lenmin, self.lenmax))
        super().__set__(instance, value)

class SizedString(StringType, SizedBase):
    pass


class Optioned(Descriptor):
    def __init__(self, options, **kwargs):
        super().__init__(**kwargs)
        self.options = options

    def __set__(self, instance, value):
        if not value in self.options:
            raise Exception('==> NOT AN OPTION')
        super().__set__(instance, value)




CONFIG = {
    'a': Optioned(options=(1, 2), attr='a'),
}


class BaseNameMeta(type):
    pass
    def __new__(cls, name, bases, namespace):
        newnamespace = {}
        for attr, attrtype in namespace['conf'].items():
            newnamespace[attr] = attrtype
        newcls = type.__new__(cls, name, bases, newnamespace)
        return newcls

class BaseName(metaclass=BaseNameMeta):
    conf = CONFIG


name = BaseName()
name.a = 1
# print(dir(name))
# print(vars(name))
# print(vars(BaseName))
# print(BaseName.members)
# print(name.members)

# class TEMP:
#     k = SizedString(lenmin=2, lenmax=3)

# t = TEMP()
# t.k = 1

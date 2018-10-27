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

class SizedStrBase(Descriptor):
    def __init__(self, lenmin, lenmax, **kwargs):
        super().__init__(**kwargs)
        self.lenmin = lenmin
        self.lenmax = lenmax

    def __set__(self, instance, value):
        if not self.lenmin <= len(value) <= self.lenmax:
            raise Exception('==> MUST BE LENGTH: %i - %i' % (self.lenmin, self.lenmax))
        super().__set__(instance, value)

class SizedString(StringType, SizedStrBase):
    pass


class LimitedIntBase(Descriptor):
    def __init__(self, minint, maxint, **kwargs):
        super().__init__(**kwargs)
        self.minint = minint
        self.maxint = maxint

    def __set__(self, instance, value):
        if not self.minint <= value <= self.maxint:
            raise Exception('==> MUST BE  %i < x < %i' % (self.minint, self.maxint))
        super().__set__(instance, value)


class LimitedInt(IntType, LimitedIntBase):
    pass

# =================================================
class K:
    l = LimitedInt(minint=3, maxint=7, attr='l')

k = K()
k.l = 4
# =================================================

class Optioned(Descriptor):
    def __init__(self, options, **kwargs):
        super().__init__(**kwargs)
        self.options = options

    def __set__(self, instance, value):
        if not value in self.options:
            raise Exception('==> NOT AN OPTION')
        super().__set__(instance, value)




CONFIG = {
    'a': {'choices': (1, 2)}
}


class BaseNameMeta(type):
    pass
    def __new__(cls, name, bases, namespace):
        newnamespace = {}
        for attr, attrtype in namespace['conf'].items():
            if tuple(attrtype.keys())[0] == 'choices':
                choices = tuple(attrtype.values())[0]
                newnamespace[attr] = Optioned(options=choices, attr=attr)

        newcls = type.__new__(cls, name, bases, newnamespace)
        return newcls



class BaseName(metaclass=BaseNameMeta):
    conf = CONFIG


name = BaseName()
name.a = 2
name.b = 0

# name.a = 0
# name.b = 0
# print(dir(name))
# print(vars(name))
# print(vars(BaseName))
# print(BaseName.members)
# print(name.members)

# class TEMP:
#     k = SizedString(lenmin=2, lenmax=3)

# t = TEMP()
# t.k = 1

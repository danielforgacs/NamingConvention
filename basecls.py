# module to create sanity checked strings like
# product names. The string consist of multiple
# elements. Rules for the elements come
# from a configuration.


class Descriptor:
    """
    Root descriptor class. All elements are set here
    if they passed the tests in the subclasses.
    The attributes name must be added.
    """
    def __init__(self, attr):
        self.attr = attr

    def __get__(self, instance, cls):
        if self.attr not in instance.__dict__:
            return None
        return instance.__dict__[self.attr]

    def __set__(self, instance, value):
        instance.__dict__[self.attr] = value


class TypeBase(Descriptor):
    """
    This class checkes if the attribute is the
    right type. Types are set in the sublcasses
    "typebase" attribute.
    """
    def __set__(self, instance, value):
        if not isinstance(value, self.typebase):
            raise Exception('==> MUST BE TYPE: '+str(self.typebase))
        super().__set__(instance, value)


class StringType(TypeBase):
    typebase = str

class IntType(TypeBase):
    typebase = int


class SizedStrBase(Descriptor):
    """
    Base class testing the lenght of a string.
    Lenght is configured with the "lenmin"
    and "lenmax" attributes.
    """
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
    """
    Base class for testing integer limits.
    Limits are configured with the "minint"
    and "maxint" attrs.
    """
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


class Optioned(Descriptor):
    """
    Main class for elements that have options.
    Options are configured with the "options"
    argument. "options" must be sequence type.
    """
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
    """
    Metaclass to create the string classes.
    It populates class dictionaries with elements
    configured in the "conf" attr in the classes.
    """
    def __new__(cls, name, bases, namespace):
        for attr, attrtype in namespace['conf'].items():
            if tuple(attrtype.keys())[0] == 'choices':
                choices = tuple(attrtype.values())[0]
                namespace[attr] = Optioned(options=choices, attr=attr)

        newcls = type.__new__(cls, name, bases, namespace)
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

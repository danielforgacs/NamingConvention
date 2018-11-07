class Descriptor(object):
    def __init__(self, attr):
        self.attr = attr

    def __set__(self, instance, value):
        instance.__dict__[self.attr] = value

    def __get__(self, instance, cls):
        if self.attr not in instance.__dict__.keys():
            return None
        return instance.__dict__[self.attr]



class TypedAttr(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, self.attrtype):
            value = None
        super().__set__(instance, value)



class StringTyped(TypedAttr):
    attrtype = str



class IntTyped(TypedAttr):
    attrtype = int



class LimitedIntBase(Descriptor):
    def __set__(self, instance, value):
        if not self.intmin <= value <= self.intmax:
            value = None
        super().__set__(instance, value)



class LimitedInt(IntTyped, LimitedIntBase):
    def __init__(self, intmin, intmax, **kwargs):
        super().__init__(**kwargs)
        self.intmin, self.intmax = intmin, intmax



class LenLimitBase(Descriptor):
    def __set__(self, instance, value):
        if not self.lenmin <= len(value) <= self.lenmax:
            value = None
        super().__set__(instance, value)



class LimitedString(StringTyped, LenLimitBase):
    def __init__(self, lmin, lmax, **kwargs):
        super().__init__(**kwargs)
        self.lenmin, self.lenmax = lmin, lmax



class OptionedAttr(Descriptor):
    def __init__(self, options, **kwargs):
        super().__init__(**kwargs)
        self.options = options

    def __set__(self, instance, value):
        if value not in self.options:
            value = None
        super(OptionedAttr, self).__set__(instance, value)



class NameMeta(type):
    def __new__(cls, name, bases, namespace):
        for attr, value in namespace['config'].items():
            attrtype = tuple(value.keys())[0]
            values = value[attrtype]
            kwargs = {'attr': attr}

            if attrtype == 'text':
                namespace[attr] = StringTyped(**kwargs)

            elif attrtype == 'limitedtext':
                kwargs['lmin'] = values[0]
                kwargs['lmax'] = values[1]
                namespace[attr] = LimitedString(**kwargs)

            elif attrtype == 'integer':
                namespace[attr] = IntTyped(**kwargs)

            elif attrtype == 'limitedinteger':
                kwargs['intmin'] = values[0]
                kwargs['intmax'] = values[1]
                namespace[attr] = LimitedInt(**kwargs)

            elif attrtype == 'options':
                kwargs['options'] = values
                namespace[attr] = OptionedAttr(**kwargs)

            else:
                raise Exception('ATTR TYPE NOT IMPLEMENTED')

        return type(name, bases, namespace)



class NameBase(object):
    @property
    def name(self):
        if not self:
            return None
        result = '_'.join([str(getattr(self, attr)) for attr in self.config.keys()])
        return result

    def __nonzero__(self):
        result = all([getattr(self, attr) for attr in self.config.keys()])
        return result






VARIANTCONF = {
    'integer': {'integer': None},
    'limitedinteger': {'limitedinteger': (100, 200)},
    'text': {'text': None},
    'limitedtext': {'limitedtext': (1, 2)},
    'region': {'options': ('aaa', 'bbb')},
}

class VariantName(NameBase, metaclass=NameMeta):
    __metaclass__ = NameMeta
    config = VARIANTCONF






if __name__ == '__main__':
    pass

    variant = VariantName()
    variant.text = '1234'
    variant.integer = 123
    variant.limitedinteger = 200
    variant.limitedtext = '12'
    variant.region = 'aaa'

    print(variant.text)
    print(variant.integer)
    print(variant.limitedinteger)
    print(variant.limitedtext)
    print(variant.region)
    print()
    print(bool(variant))
    print(variant.name)

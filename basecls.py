class Descriptor:
    def __get__(self, instance, cls):
        return instance.__dict__['source']

    def __set__(self, instance, value):
        instance.__dict__['source'] = value


class StringType(Descriptor):
    def __set__(self, instance, value):
        print('aghslfdgh')
        print('aghslfdgh')
        print('aghslfdgh')
        print('aghslfdgh')
        if not isinstance(value, str):
            raise Exception('==> MUST BE STRING')

        super().__set__(instance, value)



class BaseName:
    source = StringType()




# c = BaseName()
# c.source = 1
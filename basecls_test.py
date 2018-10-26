import basecls
import pytest



@pytest.mark.parametrize('value', (
    1, (), [], 1.23,
    ))
def test_StringType_is_string_only(value):
    class TestClass:
        testattr = basecls.StringType(attr='testattr')

    name = TestClass()
    name.testattr = '123'

    with pytest.raises(Exception):
        name.testattr = value



@pytest.mark.parametrize('value', (
    '1', (), [], 1.23,
    ))
def test_IntType_is_int_only(value):
    class TestClass:
        testattr = basecls.IntType(attr='testattr')

    name = TestClass()
    name.testattr = 123

    with pytest.raises(Exception):
        name.testattr = value



@pytest.mark.parametrize('value', (
    '',
    'a',
    'aaaa',
    1,
    ))
def test_SizedString_has_limited_lenght(value):
    class TestClass:
        testattr = basecls.SizedString(
            attr='testattr',
            lenmin=2,
            lenmax=3)

    name = TestClass()
    name.testattr = '12'

    with pytest.raises(Exception):
        name.testattr = value


@pytest.mark.parametrize('value', (
    1, 'x', '23fks',
    ))
def test_optioned(value):
    class TestClass:
        testattr = basecls.Optioned(
            attr='testattr',
            options=('a', 'b'))

    name = TestClass()
    name.testattr = 'a'

    assert name.testattr == 'a'

    name.testattr = 'b'

    assert name.testattr == 'b'

    with pytest.raises(Exception):
        name.testattr = value



if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

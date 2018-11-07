import pytest
import basecls



@pytest.mark.parametrize('type_, value', (
    (int, 12345),
    (str, 'skjdhf'),
    (tuple, (1, 2, 3)),
    (list, [1, 2, 3]),
    (float, 1.234)
    ))
def test_typed_class(type_, value):
    class TestType(basecls.TypedAttr):
        attrtype = type_

    class TestName(object):
        testattr = TestType(attr='testattr')

    testname = TestName()
    testname.testattr = value



def test_LenLimited_class_01():
    class LenLimited(basecls.LenLimitBase):
        lenmin, lenmax = 2, 3

    class TestName(object):
        testattr = LenLimited(attr='testattr')

    testname = TestName()
    testname.testattr = '123'



@pytest.mark.parametrize('lmin, lmax, value', (
    (2, 3, '1'),
    (2, 3, '1234'),
    ))
def test_LenLimited_class_02(lmin, lmax, value):
    class LenLimited(basecls.LenLimitBase):
        lenmin, lenmax = lmin, lmax

    class TestName(object):
        testattr = LenLimited(attr='testattr')

    testname = TestName()
    testname.testattr = value

    assert testname.testattr == None



@pytest.mark.parametrize('value', (
    2, 3, 'aaa'
    ))
def test_OptionedAttr_01(value):
    class OptionedAttrTest(object):
        testattr = basecls.OptionedAttr(attr='testattr', options=(2, 3, 'aaa'))

    testname = OptionedAttrTest()
    testname.testattr = value



@pytest.mark.parametrize('value', (
    1, 33, 'b'
    ))
def test_OptionedAttr_02(value):
    class OptionedAttrTest(object):
        testattr = basecls.OptionedAttr(attr='testattr', options=(2, 3, 'aaa'))

    testname = OptionedAttrTest()
    testname.testattr = value

    assert testname.testattr == None







if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

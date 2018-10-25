import basecls
import pytest



@pytest.mark.parametrize('typ', (
    1, (), [], 1.23
    ))
def test_source_is_string(typ):
    name = basecls.BaseName()
    name.source = '123'

    with pytest.raises(Exception):
        name.source = typ


@pytest.mark.parametrize('typ', (
    '1', (), [], 1.23
    ))
def test_count_is_int(typ):
    name = basecls.BaseName()
    name.count = 1

    with pytest.raises(Exception):
        name.count = typ




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

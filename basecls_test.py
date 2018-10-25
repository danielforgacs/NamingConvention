import basecls
import pytest



def test_source_is_string():
    name = basecls.BaseName()
    name.source = '123'

    for typ in (1, (), [], 1.23):
        with pytest.raises(Exception):
            name.source = typ


def test_count_is_int():
    name = basecls.BaseName()
    name.count = 1

    for typ in ('1', (), [], 1.23):
        with pytest.raises(Exception):
            name.count = typ




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

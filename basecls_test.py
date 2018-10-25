import basecls
import pytest



def test_source_is_string():
    name = basecls.BaseName()

    for typ in (1, (), [], 1.23):
        with pytest.raises(Exception):
            name.source = typ




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

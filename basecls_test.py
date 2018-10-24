import basecls
import pytest



def test_source_is_string():
    name = basecls.BaseName()

    with pytest.raises(Exception):
        name.source = 1




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

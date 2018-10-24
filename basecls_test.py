import basecls
import pytest


def test_01():
    name = basecls.BaseName()


if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

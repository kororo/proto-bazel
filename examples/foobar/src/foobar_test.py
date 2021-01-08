import sys

import pytest


def test_foobar() -> None:
	assert 1 == 1


if __name__ == "__main__":
	sys.exit(pytest.main([__file__]))

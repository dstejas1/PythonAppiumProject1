import pytest

@pytest.fixture(scope="module")
def setup():
    print("DB connection start")

    yield
    print("DB connection end")

@pytest.fixture(scope="function")
def before_eac_function():
    print("start driver connection")

    yield
    print("end driver connection")

def test_login(setup):
    print("test login")

def test_logout(before_eac_function):
    print("test_logout")
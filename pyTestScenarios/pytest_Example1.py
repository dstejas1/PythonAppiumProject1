import pytest

@pytest.mark.order(1)
def test_login():
    print("This is login test")


@pytest.mark.order(5)
def test_logout():
    print("This is logout test")


@pytest.mark.order(2)
def test_search_app():
    print("This is searchApp test")


@pytest.mark.order(3)
def test_createUser():
    print("This is createUser test")


@pytest.mark.order(4)
def test_deleteUser():
    print("This is deleteUser test")
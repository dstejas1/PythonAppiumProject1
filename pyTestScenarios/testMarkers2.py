import pytest
def test_data():
    return {
        ("tejas1@user.com","1234"),
        ("tejas2@user.com","1234")
    }
@pytest.mark.parametrize("username","password", test_data())
def test_login(username,password):
    print(username,"...", password)
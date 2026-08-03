import pytest


@pytest.mark.sanity
def test_login():
    print("test login")

@pytest.mark.smoke
def test_logout():
    print("test_logout")

@pytest.mark.reg
def test_create():
    print("test_create")

@pytest.mark.skip
def test_edit():
    print("edit_flow")
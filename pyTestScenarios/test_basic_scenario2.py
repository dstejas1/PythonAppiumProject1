import pytest



def setup_module(module):
    print("DB connection start")
def tear_down(module):
    print("DB connection end")


def setup_function(function):
    print("start appium_server")

def teardown_function(function):
    print("stop server")

def test_login():
    print("test login")

def test_logout():
    print("test_logout")
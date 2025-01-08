import pytest

from safe_calculator import SafeCalculator


def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    left = 1
    right = 2
    
    x = SafeCalculator(Authorizer("1456", "admin")).add(left,right)
    assert x == left + right


class Authorizer:
    
    def __init__(self, password, rank):
        self.password = password
        self.rank = rank
        self.correct_credentials = False
        self.token = None
    
    def login(self):
        # Asserting credentials are correct
        self.token = ((int(self.password) + 13) * 37) % 43
        return self.correct_credentials
        
    def authorize(self):
        if self.login() and self.token is not None and self.rank == "admin":
            return True
        
        

import pytest

from safe_calculator import SafeCalculator


def test_add():
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
        
    def authorize(self):
        return True
        
        

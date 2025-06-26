import pytest
from MathX.core import *

def test_is_prime():
    assert isPrime(2) == True
    assert isPrime(10) == False

def test_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(0) == 0

def test_is_palindrome():
    assert isPalindrome(121) == True
    assert isPalindrome("madam") == True

def test_gcd_lcm():
    assert gcdMultiple(36, 48) == 12
    assert lcmMultiple(12,8) == 24

def test_mean():
    assert arithmeticMean(12,6,3) == 7
    assert geometricMean(1,36) == 6

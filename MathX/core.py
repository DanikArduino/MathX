import math
from typing import List, Union, Dict

def isPrime(number : int) -> bool:
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True

def prime(number: int) -> int:
    count = 0
    num = 2
    while True:
        if isPrime(num):
            count += 1
            if count == number:
                return num
        num += 1


def primeSubsequence(start : int, finish: int) -> List[int]:
    result = []
    for i in range(max(2,start), finish):
        if isPrime(i):
            result.append(i)

    return result

def primeSubsequenceQuantity(start : int, finish: int) -> List[int]:
    result = []
    for i in range(max(1,start), finish):
        result.append(prime(i))

    return result

def fibonacci(number : int, mode : bool = 0) -> int: # 0 - с нуля, 1 - с единицы
    a,b = 0,1
    if not mode:
        for i in range(number - 1):
            a,b = b, a+b
    else :
        for i in range(number):
            a,b = b, a+b
    return a

def isFibonacci(number : int) -> bool:
    def perfectSquare(n):
        s = int(math.sqrt(n))
        return s * s == n

    if number < 0:
        return False

    check = 5 * number * number
    return perfectSquare(check + 4) or perfectSquare(check - 4)



def fibonacciSubsequence(start : int, finish : int, mode : bool = 0) -> List[int]: # 0 - с нуля, 1 - с единицы
    result = []
    for i in range(start, finish):
        # if isFibonacci(i):
        #     result.append(i)
        if fibonacci(i, mode) < finish:
            result.append(fibonacci(i, mode))

    return result

def fibonacciSubsequenceQuantity(start : int, finish : int, mode : bool = 0) -> List[int]: # 0 - с нуля, 1 - с единицы
    result = []
    for i in range(start, finish):
        result.append(fibonacci(i, mode))

    return result

def isPalindrome(ent : Union[int, str]) -> bool:
    ent = str(ent)
    return ent == ent[::-1]

def factorize(number: int) -> Dict[int, int]:
    factors = {}
    count = 0
    while number % 2 == 0:
        count += 1
        number = number // 2
    if count > 0:
        factors[2] = count
    i = 3
    while i <= math.sqrt(number):
        count = 0
        while number % i == 0:
            count += 1
            number = number // i
        if count > 0:
            factors[i] = count
        i += 2
    if number > 2:
        factors[number] = 1
    return factors


def gcdMultiple(*args):   # НОД
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = args[0]
    for num in args[1:]:
        result = gcd(result, num)
    return result

def lcmMultiple(*args): # НОК
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    result = 1
    for num in args:
        result = result * num // gcd(result, num)
    return result

def arithmeticMean(*args):
    n = len(args)
    return sum(args) / n

def geometricMean(*args):
    product = 1
    for i in args:
        product *= i
    return math.sqrt(product)


print(geometricMean(12, 10)) # 11
print(geometricMean(12, 10, 8)) # 10
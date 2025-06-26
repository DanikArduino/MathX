# MathX
****

## English documentation:
The MathX library is an add-on for the math library. It is designed for more complex tasks: **finding palindromes, GCD, LCM, prime numbers, Fibonacci numbers, etc.**
****

+ **isPrime(number : int)** - returns whether a number is prime (True, False) 
+ **prime(number : int)** - returns the n-th prime number
+ **primeSubsequence(start : int, finish : int)** - returns a series of prime numbers from start to finish
+ **primeSubsequenceQuantity(start : int, finish : int)** - returns a series of prime numbers starting with the prime number start and ending with the prime number finish
+ **isFibonacci(number : int)** - returns whether the entered number is a Fibonacci number
+ **fibonacci(number : int, mode : bool = 0)** - returns the n-th Fibonacci number (if mode = 0, then the count starts from zero, otherwise from one)
+ **fibonacciSubsequence(start : int, finish : int, mode : bool = 0)** - returns a series of Fibonacci numbers from start to finish (if mode = 0, then the count starts from zero, otherwise from one)
+ **fibonacciSubsequenceQuantity(start : int, finish : int, mode : bool = 0)** - returns a series of Fibonacci numbers starting with the Fibonacci number start and ending with the Fibonacci number finish (if mode = 0, then the count starts from zero, otherwise from one)
+ **isPalindrome(ent : Union[int, str])** - returns whether a number is a palindrome
+ **factorize(number : int)** - factorizes a number into prime factors
+ **gcdMultiple(args)** - returns the GCD of numbers
+ **lcmMultiple(args)** - returns the LCM of numbers
+ **arithmeticMean(args)** - returns the arithmetic mean of numbers
+ **geometricMean(args)** - returns the geometric mean of numbers

***

### Example code
```python
# Series of prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67
# Fibonacci number series(mode = 0): 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584

from MathX import *

print(isPrime(5))     # True
print(isPrime(8))    # False

print(prime(8))   # 19

print(primeSubsequence(2, 20))   # 2, 3, 5, 7, 11, 13, 17, 19

print(primeSubsequenceQuantity(0, 20))   # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67

print(isFibonacci(7))     # False
print(isFibonacci(34))    # True

print(fibonacci(5, 0))   # 3
print(fibonacci(5, 1))   # 5

print(fibonacciSubsequence(0, 20, 0))   # 0, 0, 1, 1, 2, 3, 5, 8, 13
print(fibonacciSubsequence(0, 20, 1))   # 0, 1, 1, 2, 3, 5, 8, 13

print(fibonacciSubsequenceQuantity(0, 20, 0))   # 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
print(fibonacciSubsequenceQuantity(0, 20, 1))   # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

print(isPalindrome(1221))   # True
print(isPalindrome(12341))  # False
print(isPalindrome('mum'))   # True
print(isPalindrome('mama'))  # False

print(factorize(68))   # {2: 2, 17: 1}
print(factorize(43))   # {43: 1}

print(gcdMultiple(36, 48))   # 12
print(gcdMultiple(12, 16, 20))   # 4

print(lcmMultiple(36, 48))   # 144
print(lcmMultiple(12, 16, 20))   # 240

print(arithmeticMean(12, 10)) # 11
print(arithmeticMean(12, 10, 8)) # 10

print(geometricMean(12, 10)) # 10.954451150103322
print(geometricMean(12, 10, 8)) # 30.983866769659336
```
***

### How to install
```bash
pip install MathX
```
***

## Русская документация
Библиотека MathX является дополнением для библиотеки math.
Она предназначена для более сложных задач: **нахождение палиндромов,**
**НОД, НОК, простых чисел, чисел Фибоначе и т.д.**
***

### Функционал библиотеки
+ **isPrime(number : int)** - возвращает является ли число простым(True, False)   
+ **prime(number : int)** - возвращает n-ое простое число
+ **primeSubsequence(start : int, finish : int)** - возвращает ряд простых числе от start до finish
+ **primeSubsequenceQuantity(start : int, finish : int)** - возвращает ряд простых числе начиная с простого  числа под номером start и оканчивая простым числом под номером finish
+ **isFibonacci(number : int)** - возвращает является ли введенное число числом Фибоначе
+ **fibonacci(number : int, mode : bool = 0)** - возвращает n-ое число Фибоначе(если mode = 0, то отсчет идет с нуля, иначе с единицы)
+ **fibonacciSubsequence(start : int, finish : int, mode : bool = 0)** - возвращает ряд чисел Фибоначе от start до finish(если mode = 0, то отсчет идет с нуля, иначе с единицы)
+ **fibonacciSubsequenceQuantity(start : int, finish : int, mode : bool = 0)** - возвращает ряд чисел Фибоначе начиная с числа Фибоначе под номером start и оканчивая числом Фибоначе под номером finish(если mode = 0, то отсчет идет с нуля, иначе с единицы)
+ **isPalindrome(ent : Union[int, str])** - возвращает является ли число палиндромом
+ **factorize(number : int)** - раскладывает число на простые множители
+ **gcdMultiple(args)** - возвращает НОД чисел
+ **lcmMultiple(args)** - возвращает НОК чисел
+ **arithmeticMean(args)** - возвращает среднее арифметическое чисел
+ **geometricMean(args)** - возвращает среднее геометрическое чисел
***
### Пример кода
```python
# Ряд простых чисел: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67
# Ряд чисел Фибоначе(mode = 0): 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584

from MathX import *

print(isPrime(5))     # True
print(isPrime(8))    # False

print(prime(8))   # 19

print(primeSubsequence(2, 20))   # 2, 3, 5, 7, 11, 13, 17, 19

print(primeSubsequenceQuantity(0, 20))   # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67

print(isFibonacci(7))     # False
print(isFibonacci(34))    # True

print(fibonacci(5, 0))   # 3
print(fibonacci(5, 1))   # 5

print(fibonacciSubsequence(0, 20, 0))   # 0, 0, 1, 1, 2, 3, 5, 8, 13
print(fibonacciSubsequence(0, 20, 1))   # 0, 1, 1, 2, 3, 5, 8, 13

print(fibonacciSubsequenceQuantity(0, 20, 0))   # 0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
print(fibonacciSubsequenceQuantity(0, 20, 1))   # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

print(isPalindrome(1221))   # True
print(isPalindrome(12341))  # False
print(isPalindrome('mum'))   # True
print(isPalindrome('mama'))  # False

print(factorize(68))   # {2: 2, 17: 1}
print(factorize(43))   # {43: 1}

print(gcdMultiple(36, 48))   # 12
print(gcdMultiple(12, 16, 20))   # 4

print(lcmMultiple(36, 48))   # 144
print(lcmMultiple(12, 16, 20))   # 240

print(arithmeticMean(12, 10)) # 11
print(arithmeticMean(12, 10, 8)) # 10

print(geometricMean(12, 10)) # 10.954451150103322
print(geometricMean(12, 10, 8)) # 30.983866769659336
```
***

### Как установить
```bash
pip install MathX
```
***
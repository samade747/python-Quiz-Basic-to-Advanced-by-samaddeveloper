# # https://docs.google.com/document/d/19BFJFK87WLQpjkXQFnxYoOyPf6Hmc5ZqgzZaguzVBVo/edit?tab=t.0



# # 1. What is the correct way to print "Hello, World!" in Python?  
# #    a) print("Hello, World!")  
# #    b) echo("Hello, World!")  
# #    c) cout << "Hello, World!"  
# #    d) System.out.println("Hello, World!")  
# #    Correct Answer: a


# # 2. How do you define a variable `greeting` with the value "Hello" and type hint it as a string?  
# #    a) greeting: str = "Hello" 
# #    b) str greeting = "Hello"  
# #    c) greeting = "Hello" : str  
# #    d) greeting = str("Hello")  
# #    Correct Answer: a



# # 3. What is the output of `print("Python"[0])`?  
# #    a) P  
# #    b) y  
# #    c) t  
# #    d) SyntaxError  
# #    Correct Answer: a




# # 4. How do you check if a string is empty using type hints?  
# #    a) def is_empty(s: str) -> bool: return len(s) == 0  
# #    b) def is_empty(s): return len(s) == 0  
# #    c) def is_empty(str s): return len(s) == 0  
# #    d) def is_empty(s: string) -> bool: return len(s) == 0  
# #    Correct Answer: a



# # 5. What is the type hint for a list of strings?  
# #    a) list[str]  
# #    b) List[str]  
# #    c) [str]  
# #    d) list of str  
# #    Correct Answer: a


# # 6. What is the output of the following code?  
# #    name = "Alice"  
# #    age = 30  
# #    print(f"My name is {name} and I am {age} years old.")  
# #    a) My name is Alice and I am 30 years old.  
# #    b) My name is {name} and I am {age} years old.  
# #    c) SyntaxError  
# #    d) NameError  
# #    Correct Answer: a




# # 7. How do you format a float to two decimal places using f-strings?  
# #    a) f"{x:.2f}"  
# #    b) f"{x:2f}"  
# #    c) f"{x:.2}"  
# #    d) f"{x:2}"  
# #    Correct Answer: a


# # 8. What is the difference between `str.format()` and f-strings?  
# #    a) f-strings are more concise and faster  
# #    b) str.format() is more powerful  
# #    c) f-strings are only available in Python 3.6+  
# #    d) All of the above  
# #    Correct Answer: d


# # 9. How do you include a literal curly brace in an f-string?  
# #    a) Double it: {{ or }}  
# #    b) Use \ before { or }  
# #    c) It's not possible  
# #    d) Use % instead  
# #    Correct Answer: a



# # 10. What is the type hint for a function that returns an f-string?  
# #     a) def func() -> str:  
# #     b) def func() -> fstring:  
# #     c) def func() -> String:  
# #     d) def func() -> text:  
# #     Correct Answer: a


# # Section 3: Operators

# # 11. What is the output of `5 + 3 * 2`?  
# #     a) 16  
# #     b) 11  
# #     c) 8  
# #     d) 10  
# #     Correct Answer: b (due to operator precedence)




# # 12. What does the `//` operator do in Python?  
# #     a) Floor division  
# #     b) Integer division  
# #     c) Both a and b  
# #     d) Modulus  
# #     Correct Answer: c



# # 13. How do you check if two variables are equal using type hints?  
# #     a) def are_equal(x: T, y: T) -> bool: return x == y  
# #     b) def are_equal(x, y): return x == y  
# #     c) def are_equal(x: any, y: any): return x == y  
# #     d) Equality check doesn't need type hints  
# #     Correct Answer: a (using generics from typing)


# # 14. What is the result of `True and False or not False`?  
# #     a) True  
# #     b) False  
# #     c) SyntaxError  
# #     d) None  
# #     Correct Answer: a


# # 15. How do you swap two variables without using a temporary variable?  
# #     a) a, b = b, a  
# #     b) a = b; b = a  
# #     c) temp = a; a = b; b = temp  
# #     d) It's not possible  
# #     Correct Answer: a

# # Section 4: Lists and Their Methods

# # 16. What is the output of `[1, 2, 3].append(4)`?  
# #     a) [1, 2, 3, 4]  
# #     b) None  
# #     c) [4]  
# #     d) Error  
# #     Correct Answer: b (append returns None)



# # 17. How do you type hint a list of integers?  
# #     a) list[int]  
# #     b) List[int]  
# #     c) [int]  
# #     d) list of int  
# #     Correct Answer: a (in Python 3.9+



# # 18. What does `list.reverse()` do?  
# #     a) Returns a reversed list  
# #     b) Reverses the list in place  
# #     c) Both a and b  
# #     d) It's not a valid method  
# #     Correct Answer: b


# # 19. How do you create a copy of a list?  
# #     a) list.copy()  
# #     b) list[:]  
# #     c) Both a and b  
# #     d) list.clone()  
# #     Correct Answer: c


# # 20. What is the difference between `remove()` and `pop()`?  
# #     a) remove() removes by value, pop() by index  
# #     b) remove() removes by index, pop() by value  
# #     c) They are the same  
# #     d) pop() can take an index, remove() cannot  
# #     Correct Answer: a



# # Section 5: Lists, Tuples, and For Loops

# # 21. What is the main difference between lists and tuples?  
# #     a) Lists are mutable, tuples are immutable  
# #     b) Tuples are mutable, lists are immutable  
# #     c) Lists can have duplicates, tuples cannot  
# #     d) Tuples can have duplicates, lists cannot  
# #     Correct Answer: a


# # 22. How do you unpack a tuple into variables?  
# #     a) x, y, z = my_tuple  
# #     b) my_tuple.unpack(x, y, z)  
# #     c) x = my_tuple[0]; y = my_tuple[1]; z = my_tuple[2]  
# #     d) Both a and c  
# #     Correct Answer: d



# # 23. What is the output of the following code?  
# #     for i in range(3):  
# #         print(i)  
# #     a) 0 1 2  
# #     b) 1 2 3  
# #     c) 0 1  
# #     d) 3  
# #     Correct Answer: a

# # 24. How do you iterate over a list with both index and value?  
# #     a) for i, val in enumerate(my_list):  
# #     b) for i in range(len(my_list)): val = my_list[i]  
# #     c) Both a and b  
# #     d) my_list.items()  
# #     Correct Answer: c


# # 25. What is the type hint for a function that takes a list of ints and returns their sum?  
# #     a) def sum_list(nums: list[int]) -> int:  
# #     b) def sum_list(nums: List[int]) -> int:  
# #     c) Both a and b  
# #     d) def sum_list(nums) -> int:  
# #     Correct Answer: c

# # Section 6: Conditional Statements

# # 26. What is the output of the following code?  
# #     x = 10  
# #     if x > 5:  
# #         print("Greater")  
# #     else:  
# #         print("Smaller")  
# #     a) Greater  
# #     b) Smaller  
# #     c) Both  
# #     d) Neither  
# #     Correct Answer: a


# # 27. How do you use `elif` in Python?  
# #     a) if condition: ... elif condition: ... else: ...  
# #     b) if condition else condition  
# #     c) switch case  
# #     d) It's not available in Python  
# #     Correct Answer: a


# # 28. What does `zip()` do in Python?  
# #     a) Combines iterables into tuples  
# #     b) Unzips files  
# #     c) Both a and b  
# #     d) It's for compression  
# #     Correct Answer: a


# # 29. How do you sort a list of tuples by the second element?  
# #     a) sorted(my_list, key=lambda x: x[1])  
# #     b) my_list.sort(key=1)  
# #     c) sorted(my_list, by=1)  
# #     d) my_list.order_by(1)  
# #     Correct Answer: a



# # 30. What is the type hint for a function that takes an int and returns a str based on conditions?  
# #     a) def check(x: int) -> str:  
# #     b) def check(int x) -> str:  
# #     c) def check(x) -> string:  
# #     d) def check(x: integer) -> string:  
# #     Correct Answer: a


# # Section 7: Dictionaries

# # 31. How do you create a dictionary with type hints?  
# #     a) my_dict: dict[str, int] = {"a": 1, "b": 2}  
# #     b) my_dict = {"a": 1, "b": 2} : dict[str, int]  
# #     c) dict my_dict[str, int] = {"a": 1, "b": 2}  
# #     d) my_dict: {str: int} = {"a": 1, "b": 2}  
# #     Correct Answer: a


# # 32. What does `dict.get(key, default)` do?  
# #     a) Returns the value for key if key is in the dictionary, else default  
# #     b) Adds key with default if not present  
# #     c) Removes key if present  
# #     d) Returns None always  
# #     Correct Answer: a


# # 33. How do you create a dictionary comprehension?  
# #     a) {k: v for k, v in iterable}  
# #     b) dict(k: v for k, v in iterable)  
# #     c) Both a and b  
# #     d) It's not possible  
# #     Correct Answer: c



# # 34. What is the output of `{**d1, **d2}` if d1 and d2 are dictionaries?  
# #     a) Merges d2 into d1  
# #     b) Creates a new dictionary with keys from both  
# #     c) Raises an error if there are duplicate keys  
# #     d) Both b and c  
# #     Correct Answer: d


# # 35. How do you type hint a function that takes a dictionary and returns a list of its values?  
# #     a) from typing import Dict, List; def get_values(d: Dict[K, V]) -> List[V]:  
# #     b) def get_values(d: dict) -> list:  
# #     c) def get_values(d) -> list of values:  
# #     d) It's not possible without knowing K and V  
# #     Correct Answer: a (using generics)


# # Section 8: Nested Dictionaries and Error Handling

# # 36. How do you access a value in a nested dictionary?  
# #     a) d['key1']['key2']  
# #     b) d.key1.key2  
# #     c) d['key1', 'key2']  
# #     d) d.get('key1', 'key2')  
# #     Correct Answer: a




# # 37. What is the best way to handle KeyError when accessing a dictionary?  
# #     a) Use try-except  
# #     b) Use dict.get()  
# #     c) Check if key in dict  
# #     d) All of the above  
# #     Correct Answer: d


# # 38. How do you type hint a nested dictionary?  
# #     a) dict[str, dict[str, int]]  
# #     b) NestedDict[str, int]  
# #     c) {str: {str: int}}  
# #     d) There is no standard way  
# #     Correct Answer: a


# # 39. What does `raise` do in Python?  
# #     a) Raises an exception  
# #     b) Catches an exception  
# #     c) Both a and b  
# #     d) It's not a keyword  
# #     Correct Answer: a


# # 40. How do you define a custom exception with type hints?  
# #     a) class MyError(Exception): pass  
# #     b) class MyError: pass  
# #     c) MyError = Exception("MyError")  
# #     d) def MyError(): raise Exception("MyError")  
# #     Correct Answer: a

# # Section 9: Loops and User Input

# # 41. What is the difference between `for` and `while` loops?  
# #     a) for is for iterating over sequences, while is for conditional looping  
# #     b) while is for iterating over sequences, for is for conditional looping  
# #     c) They are the same  
# #     d) for can have else, while cannot  
# #     Correct Answer: a


# # 42. How do you get user input in Python?  
# #     a) input()  
# #     b) readInput()  
# #     c) getUserInput()  
# #     d) It's not possible  
# #     Correct Answer: a


# # 43. What is the type hint for user input?  
# #     a) input() -> str  
# #     b) input(str)  
# #     c) str(input())  
# #     d) input returns any type  
# #     Correct Answer: a (input always returns str)

# # 44. How do you loop until a condition is met?  
# #     a) while condition: ...  
# #     b) for i in range(inf): if not condition: break  
# #     c) Both a and b  
# #     d) Python doesn't support infinite loops  
# #     Correct Answer: c
 

# # 45. What is the purpose of `break` in loops?  
# #     a) Exits the loop prematurely  
# #     b) Skips to the next iteration  
# #     c) Both a and b depending on context  
# #     d) It's not a keyword  
# #     Correct Answer: a


# # Section 10: Functions and Decorators

# # 46. What is the correct way to define a function with type hints that takes two integers and returns their sum?  
# #     a) def add(x: int, y: int) -> int: return x + y  
# #     b) def add(x, y): return x + y  
# #     c) def add(int x, int y): return x + y  
# #     d) def add(x: integer, y: integer) -> integer: return x + y  
# #     Correct Answer: a


# # 47. How do you define a decorator that preserves the type hints of the original function?  
# #     a) Use @wraps from functools  
# #     b) It's not possible  
# #     c) Use @preserve_types  
# #     d) Decorators automatically preserve type hints  
# #     Correct Answer: a

# # 48. What is a closure in Python?  
# #     a) A function that has access to its own scope and the scope of its outer functions  
# #     b) A function that is closed and cannot be called again  
# #     c) A function with no arguments  
# #     d) A function that returns itself  
# #     Correct Answer: a


# # 49. How do you type hint a function that returns another function?  
# #     a) from typing import Callable; def func() -> Callable[[int], int]: ...  
# #     b) def func() -> function: ...  
# #     c) def func() -> (int) -> int: ...  
# #     d) It's not possible  
# #     Correct Answer: a


# # 50. What is the purpose of `*args` and `**kwargs` in functions?  
# #     a) To accept any number of positional and keyword arguments  
# #     b) To accept only positional arguments  
# #     c) To accept only keyword arguments  
# #     d) To make functions more flexible  
# #     Correct Answer: a


# # Section 11: Exception Handling

# # 51. What is the structure of a try-except block?  
# #     a) try: ... except Exception as e: ...  
# #     b) try: ... catch Exception e: ...  
# #     c) try: ... on error: ...  
# #     d) It's not needed in Python  
# #     Correct Answer: a


# # 52. How do you catch multiple exceptions?  
# #     a) except (Exception1, Exception2): ...  
# #     b) except Exception1 or Exception2: ...  
# #     c) except Exception1, Exception2: ...  
# #     d) You need separate except blocks  
# #     Correct Answer: a


# 53. What does `finally` do in try-except?  
#     a) Always executes, whether exception or not  
#     b) Executes only if no exception  
#     c) Executes only if exception  
#     d) It's optional  
#     Correct Answer: a



# 54. How do you raise a custom exception?  
#     a) raise MyError("message")  
#     b) throw MyError("message")  
#     c) error MyError("message")  
#     d) It's not possible  
#     Correct Answer: a

# 55. What is the type hint for a function that may raise an exception?  
#     a) There is no specific type hint for exceptions  
#     b) def func() -> Exception: ...  
#     c) def func() raises Exception: ...  
#     d) Use @raises decorator  
#     Correct Answer: a (type hints don't specify exceptions


# 56. How do you open a file for reading with type hints?  
#     a) with open("file.txt", "r") as f: ...  
#     b) f: TextIO = open("file.txt", "r")  
#     c) Both a and b  
#     d) File handling doesn't need type hints  
#     Correct Answer: c


# 57. What does `with` statement do?  
#     a) Ensures file is closed after use  
#     b) Opens the file  
#     c) Both a and b  
#     d) It's for context management  
#     Correct Answer: d


# 58. How do you handle file not found error?  
#     a) try: open("file.txt") except FileNotFoundError: ...  
#     b) if not os.path.exists("file.txt"): ...  
#     c) Both a and b  
#     d) Files always exist in Python  
#     Correct Answer: c


# 59. What is the mode for writing to a file?  
#     a) "w"  
#     b) "r"  
#     c) "a"  
#     d) "x"  
#     Correct Answer: a


# 60. How do you type hint the return type of a function that reads from a file?  
#     a) def read_file() -> str: ... (if reading text)  
#     b) def read_file() -> bytes: ... (if reading binary)  
#     c) Both a and b depending on mode  
#     d) File reading doesn't return anything  
#     Correct Answer: c


# Section 13: Object-Oriented Programming

# 61. What is the correct way to define a class with an initializer in Python?  
#     a) class MyClass: def __init__(self, x): self.x = x  
#     b) class MyClass: def constructor(self, x): self.x = x  
#     c) class MyClass: def __constructor__(self, x): self.x = x  
#     d) class MyClass: def init(self, x): self.x = x  
#     Correct Answer: a



# Question 1
# What is the output of the following code?
# print(type(42))
# A) <class 'str'>
# B) <class 'int'>
# C) <class 'float'>
# D) <class 'bool'>
# Correct Answer: B) <class 'int'>

# Question 2
# Which of the following is a valid variable name in Python?
# A) 2variable
# B) my_variable
# C) my-variable
# D) my variable
# Correct Answer: B) my_variable


# Question 3
# What is the result of 3 + 5 * 2 in Python?
# A) 16
# B) 13
# C) 11
# D) 10
# Correct Answer: B) 13


# Question 4
# Which data type is mutable in Python?
# A) Tuple
# B) String
# C) List
# D) Integer
# Correct Answer: C) List


# Question 5
# What does the len() function do?
# A) Returns the number of characters in a string
# B) Returns the size of a variable in bytes
# C) Returns the number of items in an iterable
# D) Both A and C
# Correct Answer: D) Both A and C


# Question 6
# What is the output of the following code?
# x = "Hello"
# print(x[1])
# A) H
# B) e
# C) l
# D) o
# Correct Answer: B) e


# Question 7
# Which operator is used for exponentiation in Python?
# A) ^
# B) **
# C) *
# D) //
# Correct Answer: B) **

# Question 8
# What will print("Python".upper()) output?
# A) python
# B) PYTHON
# C) Python
# D) PYthon
# Correct Answer: B) PYTHON

# Question 9
# How do you create a single-line comment in Python?
# A) // This is a comment
# B) # This is a comment
# C) /* This is a comment */
# D) <!-- This is a comment -->
# Correct Answer: B) # This is a comment

# Question 10
# What is the output of the following code?
# for i in range(3):
#     print(i, end=" ")
# A) 0 1 2
# B) 1 2 3
# C) 0 1 2 3
# D) 1 2
# Correct Answer: A) 0 1 2

# Question 11
# Which of the following is NOT a valid Python data type?
# A) List
# B) Dictionary
# C) Array
# D) Tuple
# Correct Answer: C) Array

# Question 12
# What is the output of the following code?
# x = 10
# y = 3
# print(x // y)
# A) 3
# B) 3.33
# C) 4
# D) 3.0
# Correct Answer: A) 3

# Question 13
# What is the output of the following code?
# if 5 > 3:
#     print("Yes")
# else:
#     print("No")
# A) Yes
# B) No
# C) Error
# D) None
# Correct Answer: A) Yes

# Question 14
# What is the output of the following code?
# x = [1, 2, 3]
# x.append(4)
# print(x)
# A) [1, 2, 3]
# B) [1, 2, 3, 4]
# C) [4, 1, 2, 3]
# D) Error
# Correct Answer: B) [1, 2, 3, 4]

# Question 15
# What is the output of the following code?
# def square(num):
#     return num * num
# print(square(4))
# A) 8
# B) 16
# C) 4
# D) Error
# Correct Answer: B) 16

# Question 16
# What is the output of the following code?
# x = (1, 2, 3)
# print(x[1])
# A) 1
# B) 2
# C) 3
# D) Error
# Correct Answer: B) 2


# Question 17
# Which of the following is immutable in Python?
# A) List
# B) Dictionary
# C) Set
# D) Tuple
# Correct Answer: D) Tuple


# Question 18
# What is the output of the following code?
# d = {'a': 1, 'b': 2}
# print(d['a'])
# A) 1
# B) 2
# C) 'a'
# D) Error
# Correct Answer: A) 1

# Question 19
# What is the output of the following code?
# s = "hello"
# print(s.upper())
# A) HELLO
# B) hello
# C) Hello
# D) hELLO
# Correct Answer: A) HELLO


# Question 20
# What is the correct way to open a file for reading in Python?
# A) open("file.txt")
# B) open("file.txt", "r")
# C) open("file.txt", "w")
# D) open("file.txt", "a")
# Correct Answer: B) open("file.txt", "r")

# Question 21
# What is the output of the following code?
# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print("Error")
# A) Error
# B) 1
# C) 0
# D) None
# Correct Answer: A) Error

# Question 22
# What is the output of the following code?
# x = [1, 2, 3]
# print(x[1:3])
# A) [1, 2]
# B) [2, 3]
# C) [1, 2, 3]
# D) [3]
# Correct Answer: B) [2, 3]


# Question 23
# What is the output of the following code?
# s = {1, 2, 3}
# s.add(4)
# print(s)
# A) {1, 2, 3}
# B) {1, 2, 3, 4}
# C) {4, 1, 2, 3}
# D) Error
# Correct Answer: B) {1, 2, 3, 4}


# Question 24
# What is the output of the following code?
# print("Python"[1:4])
# A) Pyt
# B) yth
# C) tho
# D) hon
# Correct Answer: B) yth


# Question 25
# What is the output of the following code?
# x = 5
# y = 2
# print(x ** y)
# A) 10
# B) 25
# C) 7
# D) 3
# Correct Answer: B) 25

# Question 26
# What is the output of the following code?
# while False:
#     print("Loop")
# print("Done")
# A) Loop
# B) Done
# C) Loop Done
# D) Error
# Correct Answer: B) Done

# Question 27
# What is the output of the following code?
# def greet(name="Guest"):
#     return "Hello, " + name
# print(greet())
# A) Hello, Guest
# B) Hello,
# C) Error
# D) None
# Correct Answer: A) Hello, Guest

# Question 28
# What is the output of the following code?
# x = [1, 2, 3]
# x.pop(1)
# print(x)
# A) [1, 2, 3]
# B) [1, 3]
# C) [2, 3]
# D) Error
# Correct Answer: B) [1, 3]

# Question 29
# What is the output of the following code?
# d = {'x': 10, 'y': 20}
# d['z'] = 30
# print(d)
# A) {'x': 10, 'y': 20}
# B) {'x': 10, 'y': 20, 'z': 30}
# C) {'z': 30}
# D) Error
# Correct Answer: B) {'x': 10, 'y': 20, 'z': 30}

# Question 30
# What is the output of the following code?
# s = "hello world"
# print(s.split())
# A) ['hello', 'world']
# B) ['h', 'e', 'l', 'l', 'o']
# C) 'hello world'
# D) Error
# Correct Answer: A) ['hello', 'world']

# Question 31
# What is the output of the following code?
# x = 10
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# A) Even
# B) Odd
# C) 10
# D) Error
# Correct Answer: A) Even

# Question 32
# What is the output of the following code?
# for i in range(5):
#     if i == 2:
#         continue
#     print(i, end=" ")
# A) 0 1 2 3 4
# B) 0 1 3 4
# C) 2
# D) Error
# Correct Answer: B) 0 1 3 4

# Question 33
# What is the output of the following code?
# t = (1, 2, 3)
# print(len(t))
# A) 1
# B) 2
# C) 3
# D) Error
# Correct Answer: C) 3

# Question 34
# What is the output of the following code?
# s = {1, 2, 3}
# print(2 in s)
# A) True
# B) False
# C) 2
# D) Error
# Correct Answer: A) True

# Question 35
# What is the output of the following code?
# d = {'a': 1, 'b': 2}
# print(d.get('c', 0))
# A) 0
# B) None
# C) Error
# D) 'c'
# Correct Answer: A) 0

# Question 36
# What is the output of the following code?
# s = "python"
# print(s[1:4])
# A) pyt
# B) yth
# C) tho
# D) hon
# Correct Answer: B) yth

# Question 37
# What is the output of the following code?
# x = 7
# y = 3
# print(x % y)
# A) 1
# B) 2
# C) 3
# D) 0
# Correct Answer: A) 1

# Question 38
# What is the output of the following code?
# try:
#     print("5" + 5)
# except TypeError:
#     print("Error")
# A) 10
# B) Error
# C) 55
# D) None
# Correct Answer: B) Error

# Question 39
# What is the output of the following code?
# x = [1, 2, 3]
# x.remove(2)
# print(x)
# A) [1, 2, 3]
# B) [1, 3]
# C) [2, 3]
# D) Error
# Correct Answer: B) [1, 3]

# Question 40
# What is the output of the following code?
# with open("test.txt", "w") as f:
#     f.write("Hello")
# with open("test.txt", "r") as f:
#     print(f.read())
# A) Hello
# B) Error
# C) None
# D) test.txt
# Correct Answer: A) Hello

# Question 41
# What is the output of the following code?
# x = [i for i in range(3)]
# print(x)
# A) [0, 1, 2]
# B) [1, 2, 3]
# C) [0, 1, 2, 3]
# D) Error
# Correct Answer: A) [0, 1, 2]

# Question 42
# What is the output of the following code?
# import math
# print(math.ceil(3.2))
# A) 3
# B) 4
# C) 3.2
# D) Error
# Correct Answer: B) 4

# Question 43
# What is the output of the following code?
# class MyClass:
#     def __init__(self, x):
#         self.x = x
# obj = MyClass(5)
# print(obj.x)
# A) 5
# B) MyClass
# C) Error
# D) None
# Correct Answer: A) 5

# Question 44
# What is the output of the following code?
# s = "hello"
# print(s.replace("l", "p"))
# A) heppo
# B) hello
# C) heppl
# D) Error
# Correct Answer: A) heppo

# Question 45
# What is the output of the following code?
# x = {1: 'a', 2: 'b'}
# print(x.keys())
# A) [1, 2]
# B) ['a', 'b']
# C) dict_keys([1, 2])
# D) Error
# Correct Answer: C) dict_keys([1, 2])

# Question 46
# What is the output of the following code?
# for i in range(4):
#     if i == 1:
#         break
#     print(i, end=" ")
# A) 0
# B) 0 1
# C) 0 1 2 3
# D) Error
# Correct Answer: A) 0

# Question 47
# What is the output of the following code?
# x = (1, 2, 3)
# y = x + (4,)
# print(y)
# A) (1, 2, 3)
# B) (1, 2, 3, 4)
# C) [1, 2, 3, 4]
# D) Error
# Correct Answer: B) (1, 2, 3, 4)

# Question 48
# What is the output of the following code?
# s = {1, 2, 3}
# s.discard(2)
# print(s)
# A) {1, 2, 3}
# B) {1, 3}
# C) {2}
# D) Error
# Correct Answer: B) {1, 3}

# Question 49
# What is the output of the following code?
# try:
#     x = int("abc")
# except ValueError:
#     print("Error")
# A) abc
# B) Error
# C) 0
# D) None
# Correct Answer: B) Error

# Question 50
# What is the output of the following code?
# x = [1, 2, 3]
# print(x[-1])
# A) 1
# B) 2
# C) 3
# D) Error
# Correct Answer: C) 3

# Question 52
# What is the output of the following code?
# s = "hello"
# print(s.count("l"))
# A) 1
# B) 2
# C) 3
# D) 0
# Correct Answer: B) 2

# Question 53
# What is the output of the following code?
# d = {'a': 1, 'b': 2}
# del d['a']
# print(d)
# A) {'a': 1, 'b': 2}
# B) {'b': 2}
# C) {}
# D) Error
# Correct Answer: B) {'b': 2}

# Question 54
# What is the output of the following code?
# x = [1, 2, 3]
# x.extend([4, 5])
# print(x)
# A) [1, 2, 3]
# B) [1, 2, 3, 4, 5]
# C) [4, 5, 1, 2, 3]
# D) Error
# Correct Answer: B) [1, 2, 3, 4, 5]

# Question 55
# What is the output of the following code?
# def add(a, b=10):
#     return a + b
# print(add(5))
# A) 5
# B) 10
# C) 15
# D) Error
# Correct Answer: C) 15

# Question 56
# What is the output of the following code?
# s = "python"
# print(s.startswith("py"))
# A) True
# B) False
# C) python
# D) Error
# Correct Answer: A) True

# Question 57
# What is the output of the following code?
# x = {1, 2, 3}
# y = {2, 3, 4}
# print(x.intersection(y))
# A) {1, 2, 3, 4}
# B) {2, 3}
# C) {1, 4}
# D) Error
# Correct Answer: B) {2, 3}

# Question 58
# What is the output of the following code?
# t = (1, 2, 3)
# print(t.index(2))
# A) 0
# B) 1
# C) 2
# D) Error
# Correct Answer: B) 1

# Question 59
# What is the output of the following code?
# try:
#     print(1 / 0)
# except:
#     print("Error")
# finally:
#     print("Done")
# A) Error Done
# B) Error
# C) Done
# D) Error Error
# Correct Answer: A) Error Done

# Question 60
# What is the output of the following code?
# x = [i**2 for i in range(3)]
# print(x)
# A) [0, 1, 4]
# B) [1, 4, 9]
# C) [0, 1, 2]
# D) Error
# Correct Answer: A) [0, 1, 4]

# Question 61
# What is the output of the following code?
# import random
# random.seed(1)
# print(random.randint(1, 5))
# A) 1
# B) 2
# C) 3
# D) 4
# Correct Answer: C) 3

# Question 62
# What is the output of the following code?
# class Dog:
#     def bark(self):
#         return "Woof"
# d = Dog()
# print(d.bark())
# A) Woof
# B) Dog
# C) Error
# D) None
# Correct Answer: A) Woof

# Question 63
# What is the output of the following code?
# s = "hello"
# print(s.find("x"))
# A) 0
# B) -1
# C) 1
# D) Error
# Correct Answer: B) -1

# Question 64
# What is the output of the following code?
# x = {1: 'a', 2: 'b'}
# print(x.values())
# A) [1, 2]
# B) ['a', 'b']
# C) dict_values(['a', 'b'])
# D) Error
# Correct Answer: C) dict_values(['a', 'b'])

# Question 65
# What is the output of the following code?
# for i in range(3):
#     print(i, end="")
# A) 012
# B) 123
# C) 0 1 2
# D) Error
# Correct Answer: A) 012

# Question 66
# What is the output of the following code?
# x = (1, 2, 3)
# print(x * 2)
# A) (1, 2, 3)
# B) (1, 2, 3, 1, 2, 3)
# C) [1, 2, 3, 1, 2, 3]
# D) Error
# Correct Answer: B) (1, 2, 3, 1, 2, 3)

# Question 67
# What is the output of the following code?
# s = {1, 2, 3}
# s.remove(2)
# print(s)
# A) {1, 2, 3}
# B) {1, 3}
# C) {2}
# D) Error
# Correct Answer: B) {1, 3}

# Question 68
# What is the output of the following code?
# try:
#     x = [1, 2, 3][4]
# except IndexError:
#     print("Error")
# A) 1
# B) Error
# C) 4
# D) None
# Correct Answer: B) Error

# Question 69
# What is the output of the following code?
# x = [1, 2, 3]
# print(x[::-1])
# A) [1, 2, 3]
# B) [3, 2, 1]
# C) [2, 1, 3]
# D) Error
# Correct Answer: B) [3, 2, 1]

# Question 70
# What is the output of the following code?
# x = 3
# y = 4
# print(x > y)
# A) True
# B) False
# C) 3
# D) Error
# Correct Answer: B) False

# Question 71
# What is the output of the following code?
# s = "hello"
# print(s.islower())
# A) True
# B) False
# C) hello
# D) Error
# Correct Answer: A) True

# Question 72
# What is the output of the following code?
# d = {'a': 1, 'b': 2}
# print(len(d))
# A) 1
# B) 2
# C) 3
# D) Error
# Correct Answer: B) 2

# Question 73
# What is the output of the following code?
# x = [1, 2, 3]
# x.insert(1, 4)
# print(x)
# A) [1, 2, 3]
# B) [1, 4, 2, 3]
# C) [4, 1, 2, 3]
# D) Error
# Correct Answer: B) [1, 4, 2, 3]

# Question 74
# What is the output of the following code?
# def multiply(*args):
#     result = 1
#     for x in args:
#         result *= x
#     return result
# print(multiply(2, 3))
# A) 5
# B) 6
# C) 2
# D) Error
# Correct Answer: B) 6

# Question 75
# What is the output of the following code?
# s = "python"
# print(s.endswith("on"))
# A) True
# B) False
# C) python
# D) Error
# Correct Answer: A) True

# Question 76
# What is the output of the following code?
# x = {1, 2, 3}
# y = {3, 4, 5}
# print(x.difference(y))
# A) {1, 2, 3, 4, 5}
# B) {1, 2}
# C) {3}
# D) {4, 5}
# Correct Answer: B) {1, 2}

# Question 77
# What is the output of the following code?
# t = (1, 2, 3)
# print(t.count(2))
# A) 0
# B) 1
# C) 2
# D) Error
# Correct Answer: B) 1

# Question 78
# What is the output of the following code?
# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     pass
# print("Done")
# A) Done
# B) Error
# C) 1
# D) None
# Correct Answer: A) Done

# Question 79
# What is the output of the following code?
# x = [i for i in range(5) if i % 2 == 0]
# print(x)
# A) [0, 1, 2, 3, 4]
# B) [0, 2, 4]
# C) [1, 3]
# D) Error
# Correct Answer: B) [0, 2, 4]

# Question 80
# What is the output of the following code?
# import math
# print(math.floor(3.7))
# A) 3
# B) 4
# C) 3.7
# D) Error
# Correct Answer: A) 3

# Question 81
# What is the output of the following code?
# class Cat:
#     def __init__(self, name):
#         self.name = name
# c = Cat("Whiskers")
# print(c.name)
# A) Whiskers
# B) Cat
# C) Error
# D) None
# Correct Answer: A) Whiskers


# # Advanced Python Quiz - 100 Questions
# # This quiz covers advanced Python topics, including decorators, generators, context managers, metaclasses, asynchronous programming, threading, functional programming, and more. Each question includes four answer options, with the correct answer clearly indicated.



# Question 1
# What is the purpose of a decorator in Python?
# A) To define a new function
# B) To modify the behavior of a function or class
# C) To handle exceptions
# D) To import modules
# Correct Answer: B) To modify the behavior of a function or class

# Question 2
# Which keyword is used to define a generator function?
# A) def
# B) yield
# C) return
# D) lambda
# Correct Answer: B) yield

# Question 3
# What is the output of the following code?
# def my_gen():
#     yield 1
#     yield 2
#     yield 3
# g = my_gen()
# print(next(g), next(g))
# A) 1 2
# B) 2 3
# C) 1 3
# D) Error
# Correct Answer: A) 1 2

# Question 4
# What does a context manager in Python ensure?
# A) Memory allocation
# B) Proper resource management
# C) Function execution
# D) Class definition
# Correct Answer: B) Proper resource management

# Question 5
# What is the output of the following code?
# from contextlib import contextmanager
# @contextmanager
# def my_context():
#     print("Enter")
#     yield
#     print("Exit")
# with my_context():
#     print("Inside")
# A) Enter Inside Exit
# B) Inside Enter Exit
# C) Exit Inside Enter
# D) Error
# Correct Answer: A) Enter Inside Exit

# Question 6
# What is a metaclass in Python?
# A) A class that defines the behavior of other classes
# B) A subclass
# C) An instance of a class
# D) A function that returns a class
# Correct Answer: A) A class that defines the behavior of other classes

# Question 7
# How do you define an asynchronous function in Python?
# A) Using def
# B) Using async def
# C) Using lambda
# D) Using yield
# Correct Answer: B) Using async def

# Question 8
# What is the output of the following code?
# import asyncio
# async def say_hello():
#     await asyncio.sleep(1)
#     return "Hello"
# async def main():
#     return await say_hello()
# print(asyncio.run(main()))
# A) Hello
# B) None
# C) Error
# D)
#  Correct Answer: A) Hello

# Question 9
# What does the @property decorator do?
# A) Defines a static method
# B) Converts a method into a property
# C) Makes a method private
# D) Creates a class attribute
# Correct Answer: B) Converts a method into a property

# Question 10
# What is the output of the following code?
# class MyClass:
#     def __init__(self):
#         self._x = 10
#     @property
#     def x(self):
#         return self._x
# obj = MyClass()
# print(obj.x)
# A) 10
# B) Error
# C) None
# D) _x
# Correct Answer: A) 10


# Question 11
# Which module is used for threading in Python?
# A) thread
# B) threading
# C) multiprocessing
# D) asyncio
# Correct Answer: B) threading

# Question 12
# What is the output of the following code?
# import threading
# def print_nums():
#     print(1)
# t = threading.Thread(target=print_nums)
# t.start()
# t.join()
# A) 1
# B) None
# C) Error
# D) Thread object
# Correct Answer: A) 1

# Question 13
# What is the purpose of the map() function?
# A) To filter a list
# B) To sort a list
# C) To apply a function to each item of an iterable
# D) To create a dictionary
# Correct Answer: C) To apply a function to each item of an iterable

# Question 14
# What is the output of the following code?
# nums = [1, 2, 3]
# squares = map(lambda x: x**2, nums)
# print(list(squares))
# A) [1, 4, 9]
# B) [1, 2, 3]
# C) [2, 4, 6]
# D) Error
# Correct Answer: A) [1, 4, 9]

# Question 15
# What is the difference between deepcopy and copy?
# A) copy creates a deep copy, deepcopy creates a shallow copy
# B) deepcopy creates a new compound structure, copy creates a shallow copy
# C) No difference
# D) deepcopy is for lists, copy is for dictionaries
# Correct Answer: B) deepcopy creates a new compound structure, copy creates a shallow copy

# Question 16
# What is the output of the following code?
# from copy import deepcopy
# a = [[1, 2], [3, 4]]
# b = deepcopy(a)
# b[0][0] = 5
# print(a)
# A) [[5, 2], [3, 4]]
# B) [[1, 2], [3, 4]]
# C) [[1, 2], [5, 4]]
# D) Error
# Correct Answer: B) [[1, 2], [3, 4]]

# Question 17
# What is the purpose of the __init__ method in a class?
# A) To define a static method
# B) To initialize instance attributes
# C) To create a class
# D) To destroy an object
# Correct Answer: B) To initialize instance attributes

# Question 18
# What is the output of the following code?
# class MyClass:
#     def __init__(self, x):
#         self.x = x
#     def __str__(self):
#         return f"MyClass({self.x})"
# obj = MyClass(5)
# print(obj)
# A) MyClass(5)
# B) 5
# C) Error
# D)
#  Correct Answer: A) MyClass(5)

# Question 19
# What does the @classmethod decorator do?
# A) Makes a method static
# B) Binds a method to the class rather than the instance
# C) Converts a method to a property
# D) Defines a private method
# Correct Answer: B) Binds a method to the class rather than the instance

# Question 20
# What is the output of the following code?
# class MyClass:
#     @classmethod
#     def my_method(cls):
#         return cls.__name__
# print(MyClass.my_method())
# A) MyClass
# B) my_method
# C) Error
# D) None
# Correct Answer: A) MyClass


# Question 21
# What is the purpose of the functools.partial function?
# A) To create a new function with some arguments pre-filled
# B) To decorate a function
# C) To copy a function
# D) To execute a function asynchronously
# Correct Answer: A) To create a new function with some arguments pre-filled



# Question 22
# What is the output of the following code?
# from functools import partial
# def add(x, y):
#     return x + y
# add_five = partial(add, 5)
# print(add_five(3))
# A) 8
# B) 5
# C) 3
# D) Error
# Correct Answer: A) 8


# Question 23
# What is a closure in Python?
# A) A function that retains access to variables from its enclosing scope
# B) A class method
# C) A static method
# D) A context manager
# Correct Answer: A) A function that retains access to variables from its enclosing scope


# Question 24
# What is the output of the following code?
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
# f = outer(5)
# print(f(3))
# A) 8
# B) 5
# C) 3
# D) Error
# Correct Answer: A) 8


# Question 25
# What is the purpose of the __slots__ attribute in a class?
# A) To define class methods
# B) To restrict the attributes a class can have
# C) To create static methods
# D) To initialize attributes
# Correct Answer: B) To restrict the attributes a class can have


# Question 26
# What is the output of the following code?
# class MyClass:
#     __slots__ = ['x']
#     def __init__(self):
#         self.x = 10
# obj = MyClass()
# obj.y = 20
# print(obj.y)
# A) 20
# B) 10
# C) Error
# D) None
# Correct Answer: C) Error


# Question 27
# What does the itertools.chain function do?
# A) Combines multiple iterables into a single iterable
# B) Filters an iterable
# C) Maps a function to an iterable
# D) Creates a generator
# Correct Answer: A) Combines multiple iterables into a single iterable



# Question 28
# What is the output of the following code?
# from itertools import chain
# a = [1, 2]
# b = [3, 4]
# print(list(chain(a, b)))
# A) [1, 2, 3, 4]
# B) [[1, 2], [3, 4]]
# C) [1, 2]
# D) Error
# Correct Answer: A) [1, 2, 3, 4]

# Question 29
# What is the purpose of the collections.namedtuple?
# A) To create a tuple subclass with named fields
# B) To create a dictionary
# C) To create a list
# D) To define a class
# Correct Answer: A) To create a tuple subclass with named fields

# Question 30
# What is the output of the following code?
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# A) 1
# B) 2
# C) Error
# D) None
# Correct Answer: A) 1


# Question 31
# What is the Global Interpreter Lock (GIL) in Python?
# A) A lock that prevents multiple threads from executing Python bytecode simultaneously
# B) A lock for file operations
# C) A lock for memory management
# D) A lock for asynchronous functions
# Correct Answer: A) A lock that prevents multiple threads from executing Python bytecode simultaneously

# Question 32
# What is the output of the following code?
# import multiprocessing
# def square(num):
#     return num * num
# if __name__ == '__main__':
#     with multiprocessing.Pool(2) as pool:
#         results = pool.map(square, [1, 2, 3])
#     print(results)
# A) [1, 4, 9]
# B) [1, 2, 3]
# C) Error
# D) None
# Correct Answer: A) [1, 4, 9]

# Question 33
# What is the purpose of the abc module in Python?
# A) To define abstract base classes
# B) To handle arithmetic operations
# C) To create iterators
# D) To manage threads
# Correct Answer: A) To define abstract base classes

# Question 34
# What is the output of the following code?
# from abc import ABC, abstractmethod
# class MyClass(ABC):
#     @abstractmethod
#     def my_method(self):
#         pass
# class SubClass(MyClass):
#     def my_method(self):
#         return "Hello"
# obj = SubClass()
# print(obj.my_method())
# A) Hello
# B) Error
# C) None
# D) MyClass
# Correct Answer: A) Hello

# Question 35
# What does the @staticmethod decorator do?
# A) Binds a method to the class rather than the instance
# B) Converts a method to a property
# C) Defines a method that doesn’t need a class or instance reference
# D) Makes a method private
# Correct Answer: C) Defines a method that doesn’t need a class or instance reference

# Question 36
# What is the output of the following code?
# class MyClass:
#     @staticmethod
#     def my_method():
#         return "Static"
# print(MyClass.my_method())
# A) Static
# B) Error
# C) None
# D) MyClass
# Correct Answer: A) Static

# Question 37
# What is the purpose of the weakref module?
# A) To create weak references to objects
# B) To manage memory
# C) To define weak methods
# D) To create iterators
# Correct Answer: A) To create weak references to objects

# Question 38
# What is the output of the following code?
# import weakref
# class MyClass:
#     pass
# obj = MyClass()
# ref = weakref.ref(obj)
# obj = None
# print(ref())
# A) None
# B) MyClass
# C) Error
# D)
#  Correct Answer: A) None

# Question 39
# What is the purpose of the functools.lru_cache decorator?
# A) To cache function results for performance
# B) To create a closure
# C) To define a static method
# D) To handle exceptions
# Correct Answer: A) To cache function results for performance

# Question 40
# What is the output of the following code?
# from functools import lru_cache
# @lru_cache(maxsize=2)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(5))
# A) 5
# B) 3
# C) Error
# D) None
# Correct Answer: A) 5

# Question 41
# What is the output of the following code?
# import sys
# print(sys.getsizeof([]))
# A) 56
# B) 0
# C) 8
# D) Error
# Correct Answer: A) 56

# Question 42
# What is the purpose of the __call__ method in a class?
# A) To make an instance callable like a function
# B) To initialize an instance
# C) To destroy an instance
# D) To define a static method
# Correct Answer: A) To make an instance callable like a function

# Question 43
# What is the output of the following code?
# class Callable:
#     def __call__(self):
#         return "Called"
# obj = Callable()
# print(obj())
# A) Called
# B) Error
# C) None
# D) Callable
# Correct Answer: A) Called

# Question 44
# What is the purpose of the dataclasses module?
# A) To simplify class creation with automatic methods
# B) To manage databases
# C) To create iterators
# D) To handle threads
# Correct Answer: A) To simplify class creation with automatic methods

# Question 45
# What is the output of the following code?
# from dataclasses import dataclass
# @dataclass
# class Point:
#     x: int
#     y: int
# p = Point(1, 2)
# print(p.x)
# A) 1
# B) 2
# C) Error
# D) None
# Correct Answer: A) 1

# Question 46
# What is the output of the following code?
# import operator
# nums = [1, 2, 3]
# print(operator.itemgetter(1)(nums))
# A) 1
# B) 2
# C) 3
# D) Error
# Correct Answer: B) 2

# Question 47
# What is the purpose of the enum module?
# A) To create enumerated constants
# B) To manage exceptions
# C) To define iterators
# D) To handle threads
# Correct Answer: A) To create enumerated constants

# Question 48
# What is the output of the following code?
# from enum import Enum
# class Color(Enum):
#     RED = 1
# print(Color.RED.value)
# A) 1
# B) RED
# C) Error
# D) None
# Correct Answer: A) 1

# Question 49
# What is the output of the following code?
# def my_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
# @my_decorator
# def say_hello():
#     return "hello"
# print(say_hello())
# A) HELLO
# B) hello
# C) Error
# D) None
# Correct Answer: A) HELLO

# Question 50
# What is the output of the following code?
# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
# class MyClass(metaclass=Singleton):
#     pass
# a = MyClass()
# b = MyClass()
# print(a is b)
# A) True
# B) False
# C) Error
# D) None
# Correct Answer: A) True

# Question 51
# What is the output of the following code?
# import asyncio
# async def my_task():
#     await asyncio.sleep(1)
#     return 42
# tasks = [my_task() for _ in range(2)]
# results = asyncio.run(asyncio.gather(*tasks))
# print(results)
# A) [42, 42]
# B) 42
# C) Error
# D) None
# Correct Answer: A) [42, 42]



# desh 

# Question 52
# What is the purpose of the concurrent.futures module?
# A) To manage asynchronous functions
# B) To provide a high-level interface for parallelism
# C) To define iterators
# D) To handle exceptions
# Correct Answer: B) To provide a high-level interface for parallelism

# Question 53
# What is the output of the following code?
# from concurrent.futures import ThreadPoolExecutor
# def square(n):
#     return n * n
# with ThreadPoolExecutor() as executor:
#     results = executor.map(square, [1, 2, 3])
# print(list(results))
# A) [1, 4, 9]
# B) [1, 2, 3]
# C) Error
# D) None
# Correct Answer: A) [1, 4, 9]

# Question 54
# What is the output of the following code?
# from collections import Counter
# c = Counter('hello')
# print(c['l'])
# A) 2
# B) 1
# C) 3
# D) Error
# Correct Answer: A) 2

# Question 55
# What is the purpose of the typing module?
# A) To provide type hints for static type checking
# B) To manage threads
# C) To create iterators
# D) To handle exceptions
# Correct Answer: A) To provide type hints for static type checking

# Question 56
# What is the output of the following code?
# from typing import List
# def my_func(nums: List[int]) -> int:
#     return sum(nums)
# print(my_func([1, 2, 3]))
# A) 6
# B) [1, 2, 3]
# C) Error
# D) None
# Correct Answer: A) 6

# Question 57
# What is the output of the following code?
# import re
# text = "hello world"
# print(re.sub(r'l', 'p', text))
# A) heppo worpd
# B) hello world
# C) hepp world
# D) Error
# Correct Answer: A) heppo worpd

# Question 58
# What is the purpose of the pickle module?
# A) To serialize and deserialize Python objects
# B) To manage files
# C) To create iterators
# D) To handle threads
# Correct Answer: A) To serialize and deserialize Python objects

# Question 59
# What is the output of the following code?
# import pickle
# data = [1, 2, 3]
# serialized = pickle.dumps(data)
# deserialized = pickle.loads(serialized)
# print(deserialized)
# A) [1, 2, 3]
# B) Error
# C) None
# D)
#  Correct Answer: A) [1, 2, 3]

# Question 60
# What is the output of the following code?
# class MyClass:
#     def __init__(self):
#         self._x = 10
#     @property
#     def x(self):
#         return self._x
#     @x.setter
#     def x(self, value):
#         self._x = value
# obj = MyClass()
# obj.x = 20
# print(obj.x)
# A) 20
# B) 10
# C) Error
# D) None
# Correct Answer: A) 20

# Question 61
# What is the output of the following code?
# from itertools import cycle
# c = cycle([1, 2, 3])
# print(next(c), next(c))
# A) 1 2
# B) 2 3
# C) 1 1
# D) Error
# Correct Answer: A) 1 2

# Question 62
# What is the purpose of the contextlib.suppress context manager?
# A) To suppress specified exceptions
# B) To manage threads
# C) To create iterators
# D) To define classes
# Correct Answer: A) To suppress specified exceptions

# Question 63
# What is the output of the following code?
# from contextlib import suppress
# with suppress(ZeroDivisionError):
#     print(1 / 0)
# print("Done")
# A) Done
# B) Error
# C) None
# D) 1
# Correct Answer: A) Done

# Question 64
# What is the output of the following code?
# from collections import deque
# d = deque([1, 2, 3])
# d.rotate(1)
# print(list(d))
# A) [3, 1, 2]
# B) [1, 2, 3]
# C) [2, 3, 1]
# D) Error
# Correct Answer: A) [3, 1, 2]

# Question 65
# What is the output of the following code?
# import sys
# sys.setrecursionlimit(100)
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))
# A) 120
# B) 5
# C) Error
# D) None
# Correct Answer: A) 120

# Question 66
# What is the output of the following code?
# from functools import reduce
# nums = [1, 2, 3, 4]
# print(reduce(lambda x, y: x + y, nums))
# A) 10
# B) [1, 2, 3, 4]
# C) Error
# D) None
# Correct Answer: A) 10

# Question 67
# What is the output of the following code?
# class MyClass:
#     def __init__(self):
#         self.__x = 10
#     def get_x(self):
#         return self.__x
# obj = MyClass()
# print(obj.get_x())
# A) 10
# B) Error
# C) None
# D) __x
# Correct Answer: A) 10

# Question 68
# What is the output of the following code?
# import json
# data = {'x': 1, 'y': 2}
# serialized = json.dumps(data)
# deserialized = json.loads(serialized)
# print(deserialized['x'])
# A) 1
# B) 2
# C) Error
# D) None
# Correct Answer: A) 1

# Question 69
# What is the output of the following code?
# from typing import Union
# def my_func(x: Union[int, str]) -> str:
#     return str(x)
# print(my_func(5))
# A) 5
# B) '5'
# C) Error
# D) None
# Correct Answer: B) '5'

# Question 70
# What is the output of the following code?
# import re
# text = "abc123"
# print(re.match(r'\d+', text))
# A) None
# B) <re.Match object>
# C) abc123
# D) Error
# Correct Answer: A) None

# Question 71
# What is the output of the following code?
# from collections import defaultdict
# d = defaultdict(int)
# d['x'] += 1
# print(d['x'])
# A) 1
# B) 0
# C) Error
# D) None
# Correct Answer: A) 1

# Question 72
# What is the output of the following code?
# import asyncio
# async def my_task():
#     return 42
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(my_task())
# print(result)
# A) 42
# B) Error
# C) None
# D)
#  Correct Answer: A) 42

# Question 73
# What is the output of the following code?
# from itertools import permutations
# print(list(permutations([1, 2], 2)))
# A) [(1, 2), (2, 1)]
# B) [(1, 1), (2, 2)]
# C) [(1, 2)]
# D) Error
# Correct Answer: A) [(1, 2), (2, 1)]

# Question 74
# What is the output of the following code?
# class MyClass:
#     def __init__(self):
#         self.x = 10
#     def __getattribute__(self, name):
#         return super().__getattribute__(name) * 2
# obj = MyClass()
# print(obj.x)
# A) 20
# B) 10
# C) Error
# D) None
# Correct Answer: A) 20

# Question 75
# What is the output of the following code?
# from contextlib import ExitStack
# with ExitStack() as stack:
#     stack.callback(lambda: print("Done"))
# print("Exit")
# A) Done Exit
# B) Exit Done
# C) Error
# D) None
# Correct Answer: A) Done Exit

# Question 76
# What is the output of the following code?
# import dis
# def my_func():
#     x = 1
#     y = 2
#     return x + y
# dis.dis(my_func)
# A) Bytecode instructions
# B) 3
# C) Error
# D) None
# Correct Answer: A) Bytecode instructions

# Question 77
# What is the output of the following code?
# from typing import Callable
# def my_func(f: Callable[[int], int], x: int) -> int:
#     return f(x)
# print(my_func(lambda x: x * 2, 5))
# A) 10
# B) 5
# C) Error
# D) None
# Correct Answer: A) 10

# Question 78
# What is the output of the following code?
# import time
# def my_decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         print(time.time() - start)
#     return wrapper
# @my_decorator
# def my_func():
#     time.sleep(1)
# my_func()
# A) Time elapsed
# B) Error
# C) 1
# D) None
# Correct Answer: A) Time elapsed

# Question 79
# What is the output of the following code?
# from collections import OrderedDict
# d = OrderedDict([('a', 1), ('b', 2)])
# d.move_to_end('a')
# print(list(d.keys()))
# A) ['b', 'a']
# B) ['a', 'b']
# C) Error
# D) None
# Correct Answer: A) ['b', 'a']

# Question 80
# What is the output of the following code?
# import gc
# obj = object()
# ref = weakref.ref(obj)
# obj = None
# gc.collect()
# print(ref())



# Advanced Python Quiz: 100 Questions

# Section 1: Basic Python and Strings

# 1. What is the correct way to print "Hello, World!" in Python?  
#    a) print("Hello, World!")  
#    b) echo("Hello, World!")  
#    c) cout << "Hello, World!"  
#    d) System.out.println("Hello, World!")  
#    **Correct Answer**: a) print("Hello, World!")

# 2. How do you define a variable `greeting` with the value "Hello" and type hint it as a string?  
#    a) greeting: str = "Hello"  
#    b) str greeting = "Hello"  
#    c) greeting = "Hello" : str  
#    d) greeting = str("Hello")  
#    **Correct Answer**: a) greeting: str = "Hello"

# 3. What is the output of `print("Python"[0])`?  
#    a) P  
#    b) y  
#    c) t  
#    d) SyntaxError  
#    **Correct Answer**: a) P

# 4. How do you check if a string is empty using type hints?  
#    a) def is_empty(s: str) -> bool: return len(s) == 0  
#    b) def is_empty(s): return len(s) == 0  
#    c) def is_empty(str s): return len(s) == 0  
#    d) def is_empty(s: string) -> bool: return len(s) == 0  
#    **Correct Answer**: a) def is_empty(s: str) -> bool: return len(s) == 0

# 5. What is the type hint for a list of strings?  
#    a) list[str]  
#    b) List[str]  
#    c) [str]  
#    d) list of str  
#    **Correct Answer**: a) list[str]

# Section 2: Strings and F-strings

# 6. What is the output of the following code?  
#    name = "Alice"  
#    age = 30  
#    print(f"My name is {name} and I am {age} years old.")  
#    a) My name is Alice and I am 30 years old.  
#    b) My name is {name} and I am {age} years old.  
#    c) SyntaxError  
#    d) NameError  
#    **Correct Answer**: a) My name is Alice and I am 30 years old.

# 7. How do you format a float to two decimal places using f-strings?  
#    a) f"{x:.2f}"  
#    b) f"{x:2f}"  
#    c) f"{x:.2}"  
#    d) f"{x:2}"  
#    **Correct Answer**: a) f"{x:.2f}"

# 8. What is the difference between `str.format()` and f-strings?  
#    a) f-strings are more concise and faster  
#    b) str.format() is more powerful  
#    c) f-strings are only available in Python 3.6+  
#    d) All of the above  
#    **Correct Answer**: a) f-strings are more concise and faster

# 9. How do you include a literal curly brace in an f-string?  
#    a) Double it: {{ or }}  
#    b) Use \ before { or }  
#    c) It's not possible  
#    d) Use % instead  
#    **Correct Answer**: a) Double it: {{ or }}

# 10. What is the type hint for a function that returns an f-string?  
#     a) def func() -> str:  
#     b) def func() -> fstring:  
#     c) def func() -> String:  
#     d) def func() -> text:  
#     **Correct Answer**: a) def func() -> str:

# Section 3: Operators

# 11. What is the output of `5 + 3 * 2`?  
#     a) 11  
#     b) 16  
#     c) 8  
#     d) 10  
#     **Correct Answer**: a) 11

# 12. What does the `//` operator do in Python?  
#     a) Floor division  
#     b) Integer division  
#     c) Both a and b  
#     d) Modulus  
#     **Correct Answer**: a) Floor division

# 13. How do you check if two variables are equal using type hints?  
#     a) def are_equal(x: T, y: T) -> bool: return x == y  
#     b) def are_equal(x, y): return x == y  
#     c) def are_equal(x: any, y: any): return x == y  
#     d) Equality check doesn't need type hints  
#     **Correct Answer**: a) def are_equal(x: T, y: T) -> bool: return x == y

# 14. What is the result of `True and False or not False`?  
#     a) True  
#     b) False  
#     c) SyntaxError  
#     d) None  
#     **Correct Answer**: a) True

# 15. How do you swap two variables without using a temporary variable?  
#     a) a, b = b, a  
#     b) a = b; b = a  
#     c) temp = a; a = b; b = temp  
#     d) It's not possible  
#     **Correct Answer**: a) a, b = b, a

# Section 4: Lists and Their Methods

# 16. What is the output of `[1, 2, 3].append(4)`?  
#     a) None  
#     b) [1, 2, 3, 4]  
#     c) [4]  
#     d) Error  
#     **Correct Answer**: a) None

# 17. How do you type hint a list of integers?  
#     a) list[int]  
#     b) List[int]  
#     c) [int]  
#     d) list of int  
#     **Correct Answer**: a) list[int]

# 18. What does `list.reverse()` do?  
#     a) Reverses the list in place  
#     b) Returns a reversed list  
#     c) Both a and b  
#     d) It's not a valid method  
#     **Correct Answer**: a) Reverses the list in place

# 19. How do you create a copy of a list?  
#     a) list.copy()  
#     b) list[:]  
#     c) Both a and b  
#     d) list.clone()  
#     **Correct Answer**: a) list.copy()

# 20. What is the difference between `remove()` and `pop()`?  
#     a) remove() removes by value, pop() by index  
#     b) remove() removes by index, pop() by value  
#     c) They are the same  
#     d) pop() can take an index, remove() cannot  
#     **Correct Answer**: a) remove() removes by value, pop() by index

# Section 5: Lists, Tuples, and For Loops

# 21. What is the main difference between lists and tuples?  
#     a) Lists are mutable, tuples are immutable  
#     b) Tuples are mutable, lists are immutable  
#     c) Lists can have duplicates, tuples cannot  
#     d) Tuples can have duplicates, lists cannot  
#     **Correct Answer**: a) Lists are mutable, tuples are immutable

# 22. How do you unpack a tuple into variables?  
#     a) x, y, z = my_tuple  
#     b) my_tuple.unpack(x, y, z)  
#     c) x = my_tuple[0]; y = my_tuple[1]; z = my_tuple[2]  
#     d) Both a and c  
#     **Correct Answer**: a) x, y, z = my_tuple

# 23. What is the output of the following code?  
#     for i in range(3):  
#         print(i)  
#     a) 0 1 2  
#     b) 1 2 3  
#     c) 0 1  
#     d) 3  
#     **Correct Answer**: a) 0 1 2

# 24. How do you iterate over a list with both index and value?  
#     a) for i, val in enumerate(my_list):  
#     b) for i in range(len(my_list)): val = my_list[i]  
#     c) Both a and b  
#     d) my_list.items()  
#     **Correct Answer**: a) for i, val in enumerate(my_list):

# 25. What is the type hint for a function that takes a list of ints and returns their sum?  
#     a) def sum_list(nums: list[int]) -> int:  
#     b) def sum_list(nums: List[int]) -> int:  
#     c) Both a and b  
#     d) def sum_list(nums) -> int:  
#     **Correct Answer**: a) def sum_list(nums: list[int]) -> int:

# Section 6: If, Elif, Else

# 26. What is the output of the following code?  
#     x = 10  
#     if x > 5:  
#         print("Greater")  
#     else:  
#         print("Smaller")  
#     a) Greater  
#     b) Smaller  
#     c) Both  
#     d) Neither  
#     **Correct Answer**: a) Greater

# 27. How do you use `elif` in Python?  
#     a) if condition: ... elif condition: ... else: ...  
#     b) if condition else condition  
#     c) switch case  
#     d) It's not available in Python  
#     **Correct Answer**: a) if condition: ... elif condition: ... else: ...

# 28. What does `zip()` do in Python?  
#     a) Combines iterables into tuples  
#     b) Unzips files  
#     c) Both a and b  
#     d) It's for compression  
#     **Correct Answer**: a) Combines iterables into tuples

# 29. How do you sort a list of tuples by the second element?  
#     a) sorted(my_list, key=lambda x: x[1])  
#     b) my_list.sort(key=1)  
#     c) sorted(my_list, by=1)  
#     d) my_list.order_by(1)  
#     **Correct Answer**: a) sorted(my_list, key=lambda x: x[1])

# 30. What is the type hint for a function that takes an int and returns a str based on conditions?  
#     a) def check(x: int) -> str:  
#     b) def check(int x) -> str:  
#     c) def check(x) -> string:  
#     d) def check(x: integer) -> string:  
#     **Correct Answer**: a) def check(x: int) -> str:

# Section 7: Dictionary

# 31. How do you create a dictionary with type hints?  
#     a) my_dict: dict[str, int] = {"a": 1, "b": 2}  
#     b) my_dict = {"a": 1, "b": 2} : dict[str, int]  
#     c) dict my_dict[str, int] = {"a": 1, "b": 2}  
#     d) my_dict: {str: int} = {"a": 1, "b": 2}  
#     **Correct Answer**: a) my_dict: dict[str, int] = {"a": 1, "b": 2}

# 32. What does `dict.get(key, default)` do?  
#     a) Returns the value for key if key is in the dictionary, else default  
#     b) Adds key with default if not present  
#     c) Removes key if present  
#     d) Returns None always  
#     **Correct Answer**: a) Returns the value for key if key is in the dictionary, else default

# 33. How do you create a dictionary comprehension?  
#     a) {k: v for k, v in iterable}  
#     b) dict(k: v for k, v in iterable)  
#     c) Both a and b  
#     d) It's not possible  
#     **Correct Answer**: a) {k: v for k, v in iterable}

# 34. What is the output of `{**d1, **d2}` if d1 and d2 are dictionaries?  
#     a) Creates a new dictionary with keys from both  
#     b) Merges d2 into d1  
#     c) Raises an error if there are duplicate keys  
#     d) Both b and c  
#     **Correct Answer**: a) Creates a new dictionary with keys from both

# 35. How do you type hint a function that takes a dictionary and returns a list of its values?  
#     a) from typing import Dict, List; def get_values(d: Dict[K, V]) -> List[V]:  
#     b) def get_values(d: dict) -> list:  
#     c) def get_values(d) -> list of values:  
#     d) It's not possible without knowing K and V  
#     **Correct Answer**: a) from typing import Dict, List; def get_values(d: Dict[K, V]) -> List[V]:

# Section 8: Nested Dictionary and Error Handling

# 36. How do you access a value in a nested dictionary?  
#     a) d['key1']['key2']  
#     b) d.key1.key2  
#     c) d['key1', 'key2']  
#     d) d.get('key1', 'key2')  
#     **Correct Answer**: a) d['key1']['key2']

# 37. What is the best way to handle KeyError when accessing a dictionary?  
#     a) Use dict.get()  
#     b) Use try-except  
#     c) Check if key in dict  
#     d) All of the above  
#     **Correct Answer**: a) Use dict.get()

# 38. How do you type hint a nested dictionary?  
#     a) dict[str, dict[str, int]]  
#     b) NestedDict[str, int]  
#     c) {str: {str: int}}  
#     d) There is no standard way  
#     **Correct Answer**: a) dict[str, dict[str, int]]

# 39. What does `raise` do in Python?  
#     a) Raises an exception  
#     b) Catches an exception  
#     c) Both a and b  
#     d) It's not a keyword  
#     **Correct Answer**: a) Raises an exception

# 40. How do you define a custom exception with type hints?  
#     a) class MyError(Exception): pass  
#     b) class MyError: pass  
#     c) MyError = Exception("MyError")  
#     d) def MyError(): raise Exception("MyError")  
#     **Correct Answer**: a) class MyError(Exception): pass

# Section 9: Loop and Input

# 41. What is the difference between `for` and `while` loops?  
#     a) for is for iterating over sequences, while is for conditional looping  
#     b) while is for iterating over sequences, for is for conditional looping  
#     c) They are the same  
#     d) for can have else, while cannot  
#     **Correct Answer**: a) for is for iterating over sequences, while is for conditional looping

# 42. How do you get user input in Python?  
#     a) input()  
#     b) readInput()  
#     c) getUserInput()  
#     d) It's not possible  
#     **Correct Answer**: a) input()

# 43. What is the type hint for user input?  
#     a) input() -> str  
#     b) input(str)  
#     c) str(input())  
#     d) input returns any type  
#     **Correct Answer**: a) input() -> str

# 44. How do you loop until a condition is met?  
#     a) while condition: ...  
#     b) for i in range(inf): if not condition: break  
#     c) Both a and b  
#     d) Python doesn't support infinite loops  
#     **Correct Answer**: a) while condition: ...

# 45. What is the purpose of `break` in loops?  
#     a) Exits the loop prematurely  
#     b) Skips to the next iteration  
#     c) Both a and b depending on context  
#     d) It's not a keyword  
#     **Correct Answer**: a) Exits the loop prematurely

# Section 10: Functions and Decorators

# 46. What is the correct way to define a function with type hints that takes two integers and returns their sum?  
#     a) def add(x: int, y: int) -> int: return x + y  
#     b) def add(x, y): return x + y  
#     c) def add(int x, int y): return x + y  
#     d) def add(x: integer, y: integer) -> integer: return x + y  
#     **Correct Answer**: a) def add(x: int, y: int) -> int: return x + y

# 47. How do you define a decorator that preserves the type hints of the original function?  
#     a) Use @wraps from functools  
#     b) It's not possible  
#     c) Use @preserve_types  
#     d) Decorators automatically preserve type hints  
#     **Correct Answer**: a) Use @wraps from functools

# 48. What is a closure in Python?  
#     a) A function that has access to its own scope and the scope of its outer functions  
#     b) A function that is closed and cannot be called again  
#     c) A function with no arguments  
#     d) A function that returns itself  
#     **Correct Answer**: a) A function that has access to its own scope and the scope of its outer functions

# 49. How do you type hint a function that returns another function?  
#     a) from typing import Callable; def func() -> Callable[[int], int]: ...  
#     b) def func() -> function: ...  
#     c) def func() -> (int) -> int: ...  
#     d) It's not possible  
#     **Correct Answer**: a) from typing import Callable; def func() -> Callable[[int], int]: ...

# 50. What is the purpose of `*args` and `**kwargs` in functions?  
#     a) To accept any number of positional and keyword arguments  
#     b) To accept only positional arguments  
#     c) To accept only keyword arguments  
#     d) To make functions more flexible  
#     **Correct Answer**: a) To accept any number of positional and keyword arguments

# Section 11: Try-Except

# 51. What is the structure of a try-except block?  
#     a) try: ... except Exception as e: ...  
#     b) try: ... catch Exception e: ...  
#     c) try: ... on error: ...  
#     d) It's not needed in Python  
#     **Correct Answer**: a) try: ... except Exception as e: ...

# 52. How do you catch multiple exceptions?  
#     a) except (Exception1, Exception2): ...  
#     b) except Exception1 or Exception2: ...  
#     c) except Exception1, Exception2: ...  
#     d) You need separate except blocks  
#     **Correct Answer**: a) except (Exception1, Exception2): ...

# 53. What does `finally` do in try-except?  
#     a) Always executes, whether exception or not  
#     b) Executes only if no exception  
#     c) Executes only if exception  
#     d) It's optional  
#     **Correct Answer**: a) Always executes, whether exception or not

# 54. How do you raise a custom exception?  
#     a) raise MyError("message")  
#     b) throw MyError("message")  
#     c) error MyError("message")  
#     d) It's not possible  
#     **Correct Answer**: a) raise MyError("message")

# 55. What is the type hint for a function that may raise an exception?  
#     a) There is no specific type hint for exceptions  
#     b) def func() -> Exception: ...  
#     c) def func() raises Exception: ...  
#     d) Use @raises decorator  
#     **Correct Answer**: a) There is no specific type hint for exceptions

# Section 12: Errors and File Handling

# 56. How do you open a file for reading with type hints?  
#     a) with open("file.txt", "r") as f: ...  
#     b) f: TextIO = open("file.txt", "r")  
#     c) Both a and b  
#     d) File handling doesn't need type hints  
#     **Correct Answer**: a) with open("file.txt", "r") as f: ...

# 57. What does `with` statement do?  
#     a) Ensures file is closed after use  
#     b) Opens the file  
#     c) Both a and b  
#     d) It's for context management  
#     **Correct Answer**: a) Ensures file is closed after use

# 58. How do you handle file not found error?  
#     a) try: open("file.txt") except FileNotFoundError: ...  
#     b) if not os.path.exists("file.txt"): ...  
#     c) Both a and b  
#     d) Files always exist in Python  
#     **Correct Answer**: a) try: open("file.txt") except FileNotFoundError: ...

# 59. What is the mode for writing to a file?  
#     a) "w"  
#     b) "r"  
#     c) "a"  
#     d) "x"  
#     **Correct Answer**: a) "w"

# 60. How do you type hint the return type of a function that reads from a file?  
#     a) def read_file() -> str: ... (if reading text)  
#     b) def read_file() -> bytes: ... (if reading binary)  
#     c) Both a and b depending on mode  
#     d) File reading doesn't return anything  
#     **Correct Answer**: a) def read_file() -> str: ... (if reading text)

# Section 13: Object-Oriented Programming

# 61. What is the correct way to define a class with an initializer in Python?  
#     a) class MyClass: def __init__(self, x): self.x = x  
#     b) class MyClass: def constructor(self, x): self.x = x  
#     c) class MyClass: def __constructor__(self, x): self.x = x  
#     d) class MyClass: def init(self, x): self.x = x  
#     **Correct Answer**: a) class MyClass: def __init__(self, x): self.x = x

# 62. How do you type hint the type of `self` in a class method?  
#     a) Type hinting for `self` is not necessary  
#     b) def method(self: MyClass) -> None:  
#     c) def method(self) -> None:  
#     d) def method(self: object) -> None:  
#     **Correct Answer**: a) Type hinting for `self` is not necessary

# 63. What is inheritance in OOP?  
#     a) A class derives from another class  
#     b) A class contains another class  
#     c) A class uses another class  
#     d) All of the above  
#     **Correct Answer**: a) A class derives from another class

# 64. How do you call a parent class method?  
#     a) super().method()  
#     b) parent.method()  
#     c) MyClass.method()  
#     d) It's not possible  
#     **Correct Answer**: a) super().method()

# 65. What is polymorphism?  
#     a) Different forms of the same thing  
#     b) Multiple inheritance  
#     c) Overloading methods  
#     d) All of the above  
#     **Correct Answer**: a) Different forms of the same thing

# Section 14: Advanced OOP

# 66. What is multiple inheritance?  
#     a) A class inherits from multiple classes  
#     b) A class has multiple methods  
#     c) A class is inherited by multiple classes  
#     d) It's not supported in Python  
#     **Correct Answer**: a) A class inherits from multiple classes

# 67. How do you overload methods in Python?  
#     a) Python doesn't support method overloading  
#     b) By defining methods with the same name but different parameters  
#     c) Using @overload decorator  
#     d) It's done automatically  
#     **Correct Answer**: a) Python doesn't support method overloading

# 68. What is method overriding?  
#     a) Redefining a method in a subclass  
#     b) Defining multiple methods with the same name  
#     c) Both a and b  
#     d) It's not possible in Python  
#     **Correct Answer**: a) Redefining a method in a subclass

# 69. How do you define an abstract class in Python?  
#     a) from abc import ABC, abstractmethod; class MyABC(ABC): @abstractmethod def method(self): pass  
#     b) class MyABC: def method(self): raise NotImplementedError  
#     c) Both a and b  
#     d) Python doesn't support abstract classes  
#     **Correct Answer**: a) from abc import ABC, abstractmethod; class MyABC(ABC): @abstractmethod def method(self): pass

# 70. What is the diamond problem in multiple inheritance?  
#     a) Ambiguity when two parent classes have the same method name  
#     b) When a class inherits from itself  
#     c) When there are four classes in inheritance hierarchy  
#     d) It's not an issue in Python  
#     **Correct Answer**: a) Ambiguity when two parent classes have the same method name

# Section 15: Encapsulation, Abstract Classes, and Callable

# 71. What is encapsulation in OOP?  
#     a) Bundling data and methods that operate on that data within a single unit  
#     b) Hiding internal details of an object from outside  
#     c) Both a and b  
#     d) Making all attributes public  
#     **Correct Answer**: a) Bundling data and methods that operate on that data within a single unit

# 72. How do you make an attribute private in Python?  
#     a) Prefix with __ (double underscore)  
#     b) Prefix with _ (single underscore)  
#     c) Use @private decorator  
#     d) There is no strict private in Python  
#     **Correct Answer**: a) Prefix with __ (double underscore)

# 73. What is the purpose of __str__ and __repr__?  
#     a) __str__ for user-friendly string, __repr__ for developer-friendly string  
#     b) __str__ for representation, __repr__ for printing  
#     c) They are the same  
#     d) Only __str__ is needed  
#     **Correct Answer**: a) __str__ for user-friendly string, __repr__ for developer-friendly string

# 74. How do you make an object callable?  
#     a) Define __call__ method  
#     b) Use @callable decorator  
#     c) Inherit from Callable class  
#     d) It's not possible  
#     **Correct Answer**: a) Define __call__ method

# 75. What is the type hint for a callable object?  
#     a) from typing import Callable; obj: Callable[[int], int]  
#     b) obj: function(int) -> int  
#     c) obj: (int) -> int  
#     d) There is no type hint for callables  
#     **Correct Answer**: a) from typing import Callable; obj: Callable[[int], int]

# Section 16: NumPy with nptyping

# 76. How do you type hint a NumPy array of shape (3, 4) with dtype float64?  
#     a) import numpy as np; from nptyping import NDArray, Shape; x: NDArray[Shape['3,4'], np.float64]  
#     b) x: np.array[float64, shape=(3,4)]  
#     c) x: list[list[float]]  
#     d) x: Array[float64, (3,4)]  
#     **Correct Answer**: a) import numpy as np; from nptyping import NDArray, Shape; x: NDArray[Shape['3,4'], np.float64]

# 77. What is the correct way to type hint a function that takes a NumPy array and returns its mean?  
#     a) from nptyping import NDArray; import numpy as np; def mean_array(arr: NDArray[np.float64]) -> float:  
#     b) def mean_array(arr: np.array) -> float:  
#     c) def mean_array(arr) -> np.float64:  
#     d) from typing import List; def mean_array(arr: List[float]) -> float:  
#     **Correct Answer**: a) from nptyping import NDArray; import numpy as np; def mean_array(arr: NDArray[np.float64]) -> float:

# 78. How do you create a NumPy array with type hints?  
#     a) arr: NDArray[np.int_] = np.array([1, 2, 3])  
#     b) arr = np.array([1, 2, 3]) : NDArray[np.int_]  
#     c) Both a and b  
#     d) NumPy arrays don't need type hints  
#     **Correct Answer**: a) arr: NDArray[np.int_] = np.array([1, 2, 3])

# 79. What is the purpose of nptyping?  
#     a) To provide type hints for NumPy arrays  
#     b) To create NumPy arrays  
#     c) To perform operations on NumPy arrays  
#     d) It's part of NumPy  
#     **Correct Answer**: a) To provide type hints for NumPy arrays

# 80. How do you type hint a function that returns a NumPy array?  
#     a) def func() -> NDArray[np.float64]: ...  
#     b) def func() -> np.array: ...  
#     c) def func() -> array of float: ...  
#     d) It's not possible  
#     **Correct Answer**: a) def func() -> NDArray[np.float64]: ...

# Section 17: Pandas

# 81. What is the type hint for a Pandas Series containing integers?  
#     a) from pandas import Series; s: Series[int]  
#     b) s: pd.Series[int]  
#     c) s: Series of int  
#     d) s: int Series  
#     **Correct Answer**: a) from pandas import Series; s: Series[int]

# 82. How do you create a Pandas DataFrame with type hints?  
#     a) df: DataFrame = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})  
#     b) df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]}) : DataFrame  
#     c) Both a and b  
#     d) Pandas doesn't support type hints  
#     **Correct Answer**: a) df: DataFrame = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

# 83. What does pd.read_csv() return?  
#     a) DataFrame  
#     b) Series  
#     c) Both depending on the file  
#     d) It's not a Pandas function  
#     **Correct Answer**: a) DataFrame

# 84. How do you select a column from a DataFrame with type hints?  
#     a) df['col1']: Series[int]  
#     b) df.col1: Series[int]  
#     c) Both a and b  
#     d) Column selection doesn't need type hints  
#     **Correct Answer**: a) df['col1']: Series[int]

# 85. What is the type hint for a function that takes a DataFrame and returns a Series?  
#     a) def func(df: DataFrame) -> Series:  
#     b) def func(df: pd.DataFrame) -> pd.Series:  
#     c) Both a and b  
#     d) It's not possible  
#     **Correct Answer**: a) def func(df: DataFrame) -> Series:

# Section 18: Pandas Column Functions

# 86. How do you add a new column to a DataFrame?  
#     a) df['new_col'] = values  
#     b) df.add_column('new_col', values)  
#     c) df.insert('new_col', values)  
#     d) All of the above  
#     **Correct Answer**: a) df['new_col'] = values

# 87. How do you delete a column from a DataFrame?  
#     a) df.drop('col', axis=1)  
#     b) del df['col']  
#     c) Both a and b  
#     d) df.remove('col')  
#     **Correct Answer**: a) df.drop('col', axis=1)

# 88. How do you update a column in a DataFrame?  
#     a) df['col'] = new_values  
#     b) df.update('col', new_values)  
#     c) df['col'].update(new_values)  
#     d) All of the above  
#     **Correct Answer**: a) df['col'] = new_values

# 89. What does df.rename() do?  
#     a) Renames columns or index  
#     b) Renames the DataFrame  
#     c) Both a and b  
#     d) It's not a valid method  
#     **Correct Answer**: a) Renames columns or index

# 90. How do you select rows based on a condition?  
#     a) df[df['col'] > value]  
#     b) df.query('col > value')  
#     c) Both a and b  
#     d) df.select('col > value')  
#     **Correct Answer**: a) df[df['col'] > value]

# Section 19: PandasAI

# 91. What is PandasAI primarily used for?  
#     a) Enhancing Pandas with AI-driven data analysis  
#     b) Visualizing Pandas DataFrames  
#     c) Replacing Pandas entirely  
#     d) Building machine learning models  
#     **Correct Answer**: a) Enhancing Pandas with AI-driven data analysis

# 92. How do you instantiate a PandasAI object with a DataFrame?  
#     a) from pandasai import PandasAI; pandas_ai = PandasAI(); pandas_ai.run(df, prompt="...")  
#     b) df.ai = PandasAI()  
#     c) PandasAI(df)  
#     d) It's not possible  
#     **Correct Answer**: a) from pandasai import PandasAI; pandas_ai = PandasAI(); pandas_ai.run(df, prompt="...")

# 93. What type of AI does PandasAI leverage for natural language queries?  
#     a) Large Language Models (LLMs)  
#     b) Rule-based systems  
#     c) Computer vision  
#     d) Expert systems  
#     **Correct Answer**: a) Large Language Models (LLMs)

# 94. How do you install PandasAI?  
#     a) pip install pandasai  
#     b) It's included with Pandas  
#     c) You need to build it from source  
#     d) It's not available for installation  
#     **Correct Answer**: a) pip install pandasai

# 95. What is a key benefit of using PandasAI with DataFrames?  
#     a) Allows natural language queries for data analysis  
#     b) Automatically optimizes DataFrame operations  
#     c) Replaces SQL databases  
#     d) Eliminates the need for Pandas  
#     **Correct Answer**: a) Allows natural language queries for data analysis

# Section 20: General Advanced Python and Type Hints

# 96. How do you type hint a variable that can be either an int or a str?  
#     a) from typing import Union; x: Union[int, str]  
#     b) x: int or str  
#     c) x: (int, str)  
#     d) x: any of int, str  
#     **Correct Answer**: a) from typing import Union; x: Union[int, str]

# 97. What is the purpose of the `@property` decorator?  
#     a) Allows getter and setter methods to be accessed like attributes  
#     b) Marks a method as static  
#     c) Defines an abstract method  
#     d) Restricts access to a method  
#     **Correct Answer**: a) Allows getter and setter methods to be accessed like attributes

# 98. How do you type hint a function that accepts any iterable of numbers?  
#     a) from typing import Iterable; def func(numbers: Iterable[float]) -> float:  
#     b) def func(numbers: list[float]) -> float:  
#     c) def func(numbers: any) -> float:  
#     d) def func(numbers: sequence) -> float:  
#     **Correct Answer**: a) from typing import Iterable; def func(numbers: Iterable[float]) -> float:

# 99. What is the output of the following code?  
#     def func(x, y=[]):  
#         y.append(x)  
#         return y  
#     print(func(1))  
#     print(func(2))  
#     a) [1] [1, 2]  
#     b) [1] [2]  
#     c) [1, 2] [1, 2]  
#     d) An error occurs  
#     **Correct Answer**: a) [1] [1, 2]

# 100. How do you type hint a class method that returns the instance itself?  
#     a) def method(self) -> 'MyClass':  
#     b) def method(self) -> self:  
#     c) def method(self) -> instance:  
#     d) def method(self) -> object:  
#     **Correct Answer**: a) def method(self) -> 'MyClass':






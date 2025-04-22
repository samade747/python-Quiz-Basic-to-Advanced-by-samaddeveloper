# https://docs.google.com/document/d/19BFJFK87WLQpjkXQFnxYoOyPf6Hmc5ZqgzZaguzVBVo/edit?tab=t.0



# 1. What is the correct way to print "Hello, World!" in Python?  
#    a) print("Hello, World!")  
#    b) echo("Hello, World!")  
#    c) cout << "Hello, World!"  
#    d) System.out.println("Hello, World!")  
#    Correct Answer: a


# 2. How do you define a variable `greeting` with the value "Hello" and type hint it as a string?  
#    a) greeting: str = "Hello" 
#    b) str greeting = "Hello"  
#    c) greeting = "Hello" : str  
#    d) greeting = str("Hello")  
#    Correct Answer: a



# 3. What is the output of `print("Python"[0])`?  
#    a) P  
#    b) y  
#    c) t  
#    d) SyntaxError  
#    Correct Answer: a




# 4. How do you check if a string is empty using type hints?  
#    a) def is_empty(s: str) -> bool: return len(s) == 0  
#    b) def is_empty(s): return len(s) == 0  
#    c) def is_empty(str s): return len(s) == 0  
#    d) def is_empty(s: string) -> bool: return len(s) == 0  
#    Correct Answer: a



# 5. What is the type hint for a list of strings?  
#    a) list[str]  
#    b) List[str]  
#    c) [str]  
#    d) list of str  
#    Correct Answer: a


# 6. What is the output of the following code?  
#    name = "Alice"  
#    age = 30  
#    print(f"My name is {name} and I am {age} years old.")  
#    a) My name is Alice and I am 30 years old.  
#    b) My name is {name} and I am {age} years old.  
#    c) SyntaxError  
#    d) NameError  
#    Correct Answer: a




# 7. How do you format a float to two decimal places using f-strings?  
#    a) f"{x:.2f}"  
#    b) f"{x:2f}"  
#    c) f"{x:.2}"  
#    d) f"{x:2}"  
#    Correct Answer: a


# 8. What is the difference between `str.format()` and f-strings?  
#    a) f-strings are more concise and faster  
#    b) str.format() is more powerful  
#    c) f-strings are only available in Python 3.6+  
#    d) All of the above  
#    Correct Answer: d


# 9. How do you include a literal curly brace in an f-string?  
#    a) Double it: {{ or }}  
#    b) Use \ before { or }  
#    c) It's not possible  
#    d) Use % instead  
#    Correct Answer: a



# 10. What is the type hint for a function that returns an f-string?  
#     a) def func() -> str:  
#     b) def func() -> fstring:  
#     c) def func() -> String:  
#     d) def func() -> text:  
#     Correct Answer: a


# Section 3: Operators

# 11. What is the output of `5 + 3 * 2`?  
#     a) 16  
#     b) 11  
#     c) 8  
#     d) 10  
#     Correct Answer: b (due to operator precedence)




# 12. What does the `//` operator do in Python?  
#     a) Floor division  
#     b) Integer division  
#     c) Both a and b  
#     d) Modulus  
#     Correct Answer: c



# 13. How do you check if two variables are equal using type hints?  
#     a) def are_equal(x: T, y: T) -> bool: return x == y  
#     b) def are_equal(x, y): return x == y  
#     c) def are_equal(x: any, y: any): return x == y  
#     d) Equality check doesn't need type hints  
#     Correct Answer: a (using generics from typing)


# 14. What is the result of `True and False or not False`?  
#     a) True  
#     b) False  
#     c) SyntaxError  
#     d) None  
#     Correct Answer: a


# 15. How do you swap two variables without using a temporary variable?  
#     a) a, b = b, a  
#     b) a = b; b = a  
#     c) temp = a; a = b; b = temp  
#     d) It's not possible  
#     Correct Answer: a

# Section 4: Lists and Their Methods

# 16. What is the output of `[1, 2, 3].append(4)`?  
#     a) [1, 2, 3, 4]  
#     b) None  
#     c) [4]  
#     d) Error  
#     Correct Answer: b (append returns None)



# 17. How do you type hint a list of integers?  
#     a) list[int]  
#     b) List[int]  
#     c) [int]  
#     d) list of int  
#     Correct Answer: a (in Python 3.9+



# 18. What does `list.reverse()` do?  
#     a) Returns a reversed list  
#     b) Reverses the list in place  
#     c) Both a and b  
#     d) It's not a valid method  
#     Correct Answer: b


# 19. How do you create a copy of a list?  
#     a) list.copy()  
#     b) list[:]  
#     c) Both a and b  
#     d) list.clone()  
#     Correct Answer: c


# 20. What is the difference between `remove()` and `pop()`?  
#     a) remove() removes by value, pop() by index  
#     b) remove() removes by index, pop() by value  
#     c) They are the same  
#     d) pop() can take an index, remove() cannot  
#     Correct Answer: a



# Section 5: Lists, Tuples, and For Loops

# 21. What is the main difference between lists and tuples?  
#     a) Lists are mutable, tuples are immutable  
#     b) Tuples are mutable, lists are immutable  
#     c) Lists can have duplicates, tuples cannot  
#     d) Tuples can have duplicates, lists cannot  
#     Correct Answer: a


# 22. How do you unpack a tuple into variables?  
#     a) x, y, z = my_tuple  
#     b) my_tuple.unpack(x, y, z)  
#     c) x = my_tuple[0]; y = my_tuple[1]; z = my_tuple[2]  
#     d) Both a and c  
#     Correct Answer: d



# 23. What is the output of the following code?  
#     for i in range(3):  
#         print(i)  
#     a) 0 1 2  
#     b) 1 2 3  
#     c) 0 1  
#     d) 3  
#     Correct Answer: a

# 24. How do you iterate over a list with both index and value?  
#     a) for i, val in enumerate(my_list):  
#     b) for i in range(len(my_list)): val = my_list[i]  
#     c) Both a and b  
#     d) my_list.items()  
#     Correct Answer: c


# 25. What is the type hint for a function that takes a list of ints and returns their sum?  
#     a) def sum_list(nums: list[int]) -> int:  
#     b) def sum_list(nums: List[int]) -> int:  
#     c) Both a and b  
#     d) def sum_list(nums) -> int:  
#     Correct Answer: c

# Section 6: Conditional Statements

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
#     Correct Answer: a


# 27. How do you use `elif` in Python?  
#     a) if condition: ... elif condition: ... else: ...  
#     b) if condition else condition  
#     c) switch case  
#     d) It's not available in Python  
#     Correct Answer: a


# 28. What does `zip()` do in Python?  
#     a) Combines iterables into tuples  
#     b) Unzips files  
#     c) Both a and b  
#     d) It's for compression  
#     Correct Answer: a


# 29. How do you sort a list of tuples by the second element?  
#     a) sorted(my_list, key=lambda x: x[1])  
#     b) my_list.sort(key=1)  
#     c) sorted(my_list, by=1)  
#     d) my_list.order_by(1)  
#     Correct Answer: a



# 30. What is the type hint for a function that takes an int and returns a str based on conditions?  
#     a) def check(x: int) -> str:  
#     b) def check(int x) -> str:  
#     c) def check(x) -> string:  
#     d) def check(x: integer) -> string:  
#     Correct Answer: a


# Section 7: Dictionaries

# 31. How do you create a dictionary with type hints?  
#     a) my_dict: dict[str, int] = {"a": 1, "b": 2}  
#     b) my_dict = {"a": 1, "b": 2} : dict[str, int]  
#     c) dict my_dict[str, int] = {"a": 1, "b": 2}  
#     d) my_dict: {str: int} = {"a": 1, "b": 2}  
#     Correct Answer: a


# 32. What does `dict.get(key, default)` do?  
#     a) Returns the value for key if key is in the dictionary, else default  
#     b) Adds key with default if not present  
#     c) Removes key if present  
#     d) Returns None always  
#     Correct Answer: a


# 33. How do you create a dictionary comprehension?  
#     a) {k: v for k, v in iterable}  
#     b) dict(k: v for k, v in iterable)  
#     c) Both a and b  
#     d) It's not possible  
#     Correct Answer: c



# 34. What is the output of `{**d1, **d2}` if d1 and d2 are dictionaries?  
#     a) Merges d2 into d1  
#     b) Creates a new dictionary with keys from both  
#     c) Raises an error if there are duplicate keys  
#     d) Both b and c  
#     Correct Answer: d


# 35. How do you type hint a function that takes a dictionary and returns a list of its values?  
#     a) from typing import Dict, List; def get_values(d: Dict[K, V]) -> List[V]:  
#     b) def get_values(d: dict) -> list:  
#     c) def get_values(d) -> list of values:  
#     d) It's not possible without knowing K and V  
#     Correct Answer: a (using generics)


# Section 8: Nested Dictionaries and Error Handling

# 36. How do you access a value in a nested dictionary?  
#     a) d['key1']['key2']  
#     b) d.key1.key2  
#     c) d['key1', 'key2']  
#     d) d.get('key1', 'key2')  
#     Correct Answer: a




# 37. What is the best way to handle KeyError when accessing a dictionary?  
#     a) Use try-except  
#     b) Use dict.get()  
#     c) Check if key in dict  
#     d) All of the above  
#     Correct Answer: d


# 38. How do you type hint a nested dictionary?  
#     a) dict[str, dict[str, int]]  
#     b) NestedDict[str, int]  
#     c) {str: {str: int}}  
#     d) There is no standard way  
#     Correct Answer: a


# 39. What does `raise` do in Python?  
#     a) Raises an exception  
#     b) Catches an exception  
#     c) Both a and b  
#     d) It's not a keyword  
#     Correct Answer: a


# 40. How do you define a custom exception with type hints?  
#     a) class MyError(Exception): pass  
#     b) class MyError: pass  
#     c) MyError = Exception("MyError")  
#     d) def MyError(): raise Exception("MyError")  
#     Correct Answer: a

# Section 9: Loops and User Input

# 41. What is the difference between `for` and `while` loops?  
#     a) for is for iterating over sequences, while is for conditional looping  
#     b) while is for iterating over sequences, for is for conditional looping  
#     c) They are the same  
#     d) for can have else, while cannot  
#     Correct Answer: a

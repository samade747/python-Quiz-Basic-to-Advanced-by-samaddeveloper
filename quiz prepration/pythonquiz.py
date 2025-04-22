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
#     Correct Answer: b



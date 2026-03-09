# Python Technical Quiz: 50 Questions

Python quiz: https://notebooklm.google.com/notebook/96d9fb39-de5e-4ea8-81a9-b2040b33f5c5?artifactId=b09a10f0-1ef4-4cf2-a2d5-f66333b297de

Following quiz covers fundamental to advanced Python concepts, including memory management, functional programming, object-oriented principles, asynchronous programming, memory management, and design patterns.

---

## 🟢 Level 1: Basics & Data Structures

### Question 1: List Reference

What is the output of the following code?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)

```

* **A)** `[1, 2, 3]`
* **B)** `[1, 2, 3, 4]`
* **C)** `[4, 1, 2, 3]`
* **D)** `Error`

**Answer:** **B**
**Explanation:** Lists are mutable and `y` references the same object as `x`. Modifying `y` also modifies `x` since they point to the same memory location.

---

### Question 2: Identity vs. Equality

What is the difference between `is` and `==` in Python?

* **A)** They are identical
* **B)** `is` checks identity (same object in memory), `==` checks equality (same value)
* **C)** `==` is faster than `is`
* **D)** `is` only works with strings

**Answer:** **B**
**Explanation:** `is` returns `True` if both variables point to the same object in memory. `==` returns `True` if the values are equal, regardless of whether they're the same object.

---

### Question 3: Mutable Default Arguments

What will be the output?

```python
def func(a, b=[]):
    b.append(a)
    return b

print(func(1))
print(func(2))

```

* **A)** `[1]` then `[2]`
* **B)** `[1]` then `[1, 2]`
* **C)** `[1, 2]` then `[1, 2]`
* **D)** `Error`

**Answer:** **B**
**Explanation:** Default mutable arguments are evaluated once at function definition. The same list object is reused across calls, accumulating values.

---

### Question 4: Decorators

What is a Python decorator?

* **A)** A way to add colors to output
* **B)** A function that modifies the behavior of another function without changing its source code
* **C)** A type of comment
* **D)** A class inheritance mechanism

**Answer:** **B**
**Explanation:** Decorators wrap other functions to extend or modify behavior using the `@decorator_name` syntax.

---

### Question 5: Lambda Types

What is the output?

```python
print(type(lambda x: x + 1))

```

* **A)** `<class 'lambda'>`
* **B)** `<class 'function'>`
* **C)** `<class 'method'>`
* **D)** `<class 'object'>`

**Answer:** **B**
**Explanation:** Lambda functions are anonymous functions, but their type is still `'function'` in Python.

---

## 🟡 Level 2: Intermediate Concepts

### Question 6: Arguments

What is the purpose of `*args` and `**kwargs`?

* **A)** To define required arguments
* **B)** `*args` collects positional arguments as a tuple, `**kwargs` collects keyword arguments as a dictionary
* **C)** They are deprecated
* **D)** To define class attributes

**Answer:** **B**
**Explanation:** `*args` allows passing a variable number of positional arguments. `**kwargs` allows a variable number of keyword arguments.

---

### Question 7: Generators

What is a generator in Python?

* **A)** A function that generates random numbers
* **B)** A function that uses `yield` to return an iterator that produces values lazily
* **C)** A class that generates objects
* **D)** A type of decorator

**Answer:** **B**
**Explanation:** Generators use `yield` to produce values one at a time, maintaining state between calls. They are memory-efficient for large sequences.

---

### Question 8: Scoping

What is the output?

```python
x = 10
def func():
    x = 20
    def inner():
        nonlocal x
        x = 30
    inner()
    print(x)
func()

```

* **A)** `10`
* **B)** `20`
* **C)** `30`
* **D)** `Error`

**Answer:** **C**
**Explanation:** `nonlocal` allows the inner function to modify the variable in the enclosing (non-global) scope. Thus, the middle `x` becomes `30`.

---

### Question 9: Deep vs. Shallow Copy

What is the difference between `deepcopy` and `copy`?

* **A)** They are identical
* **B)** `copy` creates a shallow copy (nested objects share references), `deepcopy` creates independent copies of all nested objects
* **C)** `deepcopy` is faster
* **D)** `copy` only works with lists

**Answer:** **B**
**Explanation:** Shallow copy creates a new object, but nested objects are still linked. Deep copy creates completely independent copies recursively.

---

### Question 10: List Comprehension

What is list comprehension and what is its advantage?

* **A)** A way to sort lists
* **B)** A concise way to create lists that is often faster and more readable than traditional loops
* **C)** A type of list method
* **D)** A way to delete list elements

**Answer:** **B**
**Explanation:** List comprehensions provide a compact syntax: `[expression for item in iterable if condition]`.

---

### Question 11: Comprehension Logic

What is the output?

```python
print([x**2 for x in range(5) if x % 2 == 0])

```

* **A)** `[0, 4, 16]`
* **B)** `[1, 9]`
* **C)** `[0, 1, 4, 9, 16]`
* **D)** `[4, 16]`

**Answer:** **A**
**Explanation:** The comprehension squares even numbers (0, 2, 4) from `range(5)`, resulting in `[0, 4, 16]`.

---

## 🔴 Level 3: Advanced & OOP

### Question 12: The GIL

What is the Global Interpreter Lock (GIL)?

* **A)** A security feature for global variables
* **B)** A mutex that allows only one thread to execute Python bytecode at a time
* **C)** A lock for file operations
* **D)** A deprecated feature

**Answer:** **B**
**Explanation:** The GIL prevents multiple native threads from executing Python bytecode simultaneously, limiting true parallelism for CPU-bound programs.

---

### Question 13: Static vs. Class Methods

What is the difference between `@staticmethod` and `@classmethod`?

* **A)** They are identical
* **B)** `@staticmethod` doesn't receive any automatic first argument; `@classmethod` receives the class as the first argument
* **C)** `@classmethod` is deprecated
* **D)** `@staticmethod` only works with strings

**Answer:** **B**
**Explanation:** `@staticmethod` is like a regular function inside a class. `@classmethod` receives the class (`cls`) as the first argument to access class state.

---

### Question 14: Class Inheritance

What is the output?

```python
class A:
    x = 1
class B(A):
    pass
class C(A):
    pass

B.x = 2
print(A.x, B.x, C.x)

```

* **A)** `1 1 1`
* **B)** `2 2 2`
* **C)** `1 2 1`
* **D)** `1 2 2`

**Answer:** **C**
**Explanation:** `B.x = 2` creates a new attribute in `B`, shadowing `A.x`. `A.x` and `C.x` (which inherits from `A`) remain `1`.

---

### Question 15: Memory Optimization

What is the purpose of `__slots__` in Python classes?

* **A)** To define method slots
* **B)** To restrict instance attributes and reduce memory usage by not using `__dict__`
* **C)** To define time slots
* **D)** To create abstract methods

**Answer:** **B**
**Explanation:** `__slots__` declares a fixed set of attributes, preventing the creation of `__dict__`. This saves memory and speeds up attribute access.

---

### Question 16: Context Managers

What is a context manager in Python?

* **A)** A memory manager
* **B)** An object implementing `__enter__` and `__exit__` for resource management (used with `with`)
* **C)** A thread manager
* **D)** A file manager only

**Answer:** **B**
**Explanation:** They handle setup and cleanup. The `with` statement calls `__enter__` on entry and `__exit__` on exit, even if errors occur.

---

### Question 17: Yielding

What is the output?

```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))

```

* **A)** `1 1`
* **B)** `1 2`
* **C)** `3 3`
* **D)** `Error`

**Answer:** **B**
**Explanation:** Each `next()` call resumes the generator from its last `yield`.

---

### Question 18: Append vs. Extend

What is the difference between `append()` and `extend()` for lists?

* **A)** They are identical
* **B)** `append` adds a single element, `extend` adds all elements from an iterable
* **C)** `extend` is deprecated
* **D)** `append` is faster

**Answer:** **B**
**Explanation:** `append(x)` adds `x` as one item. `extend(iterable)` iterates through the input and adds each item individually.

---

### Question 19: Slicing Copies

What is the output?

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)

```

* **A)** `[1, 2, 3, 4]`
* **B)** `[1, 2, 3]`
* **C)** `[4, 1, 2, 3]`
* **D)** `Error`

**Answer:** **B**
**Explanation:** `a[:]` creates a shallow copy. Modifying `b` doesn't affect `a` because they are different objects in memory.

---

### Question 20: Duck Typing

What is duck typing in Python?

* **A)** A typing module feature
* **B)** A philosophy where an object's suitability is determined by its methods, not its class type
* **C)** A way to type faster
* **D)** A testing methodology

**Answer:** **B**
**Explanation:** "If it walks like a duck and quacks like a duck, it's a duck." Python focuses on behavior over strict inheritance.

---

### Question 21: Packages

What is the purpose of `__init__.py` in a Python package?

* **A)** To initialize variables
* **B)** To mark a directory as a package and optionally execute initialization code
* **C)** To start the interpreter
* **D)** To create class instances

**Answer:** **B**
**Explanation:** It signals to Python that the directory should be treated as a package for imports.

---

### Question 22: Dict Unpacking

What is the output?

```python
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

```

* **A)** `{'a': 1, 'b': 2, 'c': 4}`
* **B)** `{'a': 1, 'b': 3, 'c': 4}`
* **C)** `{'b': 3, 'c': 4}`
* **D)** `Error`

**Answer:** **B**
**Explanation:** Dictionary unpacking merges maps. Overlapping keys take the value of the last dictionary unpacked (`y`'s `b: 3` overrides `x`'s `b: 2`).

---

### Question 23: Str vs. Repr

What is the difference between `__str__` and `__repr__`?

* **A)** They are identical
* **B)** `__str__` is for end-users (readable), `__repr__` is for developers (unambiguous)
* **C)** `__repr__` is deprecated
* **D)** `__str__` only works in Python 2

**Answer:** **B**
**Explanation:** `__str__` is for "informal" display; `__repr__` is the "official" representation used for debugging.

---

### Question 24: Descriptors

What is a Python descriptor?

* **A)** A docstring
* **B)** An object that defines `__get__`, `__set__`, or `__delete__` to customize attribute access
* **C)** A type annotation
* **D)** A decorator

**Answer:** **B**
**Explanation:** Descriptors are the underlying mechanism for properties, methods, and class methods.

---

### Question 25: Memoization

What is the output?

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(10))

```

* **A)** `55`
* **B)** `89`
* **C)** `34`
* **D)** `Error`

**Answer:** **A**
**Explanation:** `lru_cache` saves previously computed results. The 10th Fibonacci number (starting 0, 1, 1...) is `55`.

---

### Question 26: Enumerate

What is the purpose of the `enumerate()` function?

* **A)** To count elements
* **B)** To return an iterator of tuples containing index and value pairs
* **C)** To enumerate only strings
* **D)** To create numbered lists

**Answer:** **B**
**Explanation:** It allows you to loop over an iterable while having access to the current index.

---

### Question 27: Truthiness

What is the output?

```python
print(bool([]), bool([0]), bool(''), bool(' '))

```

* **A)** `False False False False`
* **B)** `False True False True`
* **C)** `True True False True`
* **D)** `False False False True`

**Answer:** **B**
**Explanation:** Empty containers (`[]`, `''`) are `False`. Non-empty containers (`[0]`, `' '`) are `True`.

---

### Question 28: Metaclasses

What is a metaclass in Python?

* **A)** A class that inherits from another
* **B)** A class of a class that defines how classes behave
* **C)** A deprecated feature
* **D)** A class decorator

**Answer:** **B**
**Explanation:** Metaclasses are the "blueprints" for classes. The default is `type`.

---

### Question 29: Concurrency

What is the difference between `multiprocessing` and `threading`?

* **A)** They are identical
* **B)** `threading` shares memory and is limited by GIL; `multiprocessing` uses separate memory and bypasses GIL
* **C)** `multiprocessing` is deprecated
* **D)** `threading` is faster for CPU-bound tasks

**Answer:** **B**
**Explanation:** Multiprocessing creates separate instances of the Python interpreter, allowing true parallel execution on multiple cores.

---

### Question 30: In-place vs. Reassignment

What is the output?

```python
x = [1, 2, 3]
y = x
x = x + [4]
print(y)

```

* **A)** `[1, 2, 3, 4]`
* **B)** `[1, 2, 3]`
* **C)** `[4, 1, 2, 3]`
* **D)** `Error`

**Answer:** **B**
**Explanation:** `x + [4]` creates a **new** list. `y` still points to the old list. If it had been `x += [4]`, `y` would have changed.

---

### Question 31: The `id()` Function

What does the `id()` function return?

* **A)** The value of the object
* **B)** The data type of the object
* **C)** A unique integer representing the object's identity (memory address in CPython)
* **D)** The variable name as a string

**Answer: C**
**Explanation:** `id()` returns a unique and constant integer for an object during its lifetime. In CPython, this corresponds to the object's address in memory.

---

### Question 32: `__call__` Method

What is the purpose of the `__call__` method in a Python class?

* **A)** To delete an object
* **B)** To allow an instance of a class to be called like a function
* **C)** To initialize class attributes
* **D)** To call a parent class method

**Answer: B**
**Explanation:** If a class implements `__call__`, you can "call" an instance (e.g., `obj()`) just like a function.

---

### Question 33: Dictionary Comprehension

What is the output of `{x: x*x for x in range(3)}`?

* **A)** `[0, 1, 4]`
* **B)** `(0, 1, 4)`
* **C)** `{0: 0, 1: 1, 2: 4}`
* **D)** `{0, 1, 4}`

**Answer: C**
**Explanation:** This is a dictionary comprehension. It maps the keys (0, 1, 2) to their squares (0, 1, 4).

---

### Question 34: `asyncio` and `await`

In asynchronous programming, what does the `await` keyword do?

* **A)** Pauses the entire program for a set time
* **B)** Suspends the execution of the current coroutine, yielding control back to the event loop
* **C)** Starts a new thread
* **D)** Forces a function to run synchronously

**Answer: B**
**Explanation:** `await` tells the event loop to pause the coroutine until the awaited task is finished, allowing other tasks to run in the meantime.

---

### Question 35: Method Resolution Order (MRO)

How does Python determine the order in which to search for methods in multiple inheritance?

* **A)** Alphabetical order of classes
* **B)** Random selection
* **C)** Using the C3 Linearization algorithm (viewable via `.mro()`)
* **D)** Depth-first search only

**Answer: C**
**Explanation:** Python uses the C3 Linearization algorithm to create a consistent Method Resolution Order (MRO) that respects inheritance hierarchies.

---

### Question 36: The `finally` Block

When is the `finally` block in a `try...except` statement executed?

* **A)** Only if an error occurs
* **B)** Only if no error occurs
* **C)** Always, regardless of whether an exception was raised or caught
* **D)** Only if the `except` block fails

**Answer: C**
**Explanation:** The `finally` block is used for cleanup actions (like closing files) and runs no matter what happened in the try/except blocks.

---

### Question 37: `dir()` Function

What does the `dir()` function do when called on an object?

* **A)** Deletes the object
* **B)** Returns a list of valid attributes and methods for that object
* **C)** Shows the file directory where the script is saved
* **D)** Reverses the object

**Answer: B**
**Explanation:** `dir()` is a powerful introspection tool that lists everything an object "knows" how to do.

---

### Question 38: Set vs. List Performance

Which operation is generally much faster in a `set` than in a `list`?

* **A)** Adding an element to the end
* **B)** Iterating through all elements
* **C)** Checking if an element exists (`item in container`)
* **D)** Sorting elements

**Answer: C**
**Explanation:** Sets use hash tables, making membership testing  on average, whereas lists require  time to search linearly.

---

### Question 39: `lambda` Arguments

Can a `lambda` function take multiple arguments?

* **A)** No, only one
* **B)** Yes, separated by commas
* **C)** Only if they are passed as a list
* **D)** No, lambdas don't take arguments

**Answer: B**
**Explanation:** A lambda can take any number of arguments but must be contained in a single expression (e.g., `lambda x, y: x + y`).

---

### Question 40: String Immutability

What happens if you try to do `s = "hello"; s[0] = "H"`?

* **A)** `s` becomes "Hello"
* **B)** It creates a new string "Hello" automatically
* **C)** TypeError: 'str' object does not support item assignment
* **D)** The string is deleted

**Answer: C**
**Explanation:** Strings in Python are immutable. You cannot change individual characters; you must create a new string instead.

---

### Question 41: `any()` and `all()`

What is the output of `any([0, False, [], 1])`?

* **A)** `True`
* **B)** `False`
* **C)** `1`
* **D)** `Error`

**Answer: A**
**Explanation:** `any()` returns `True` if at least one element in the iterable is truthy. Since `1` is truthy, it returns `True`.

---

### Question 42: `zip()` Function

What does `zip([1, 2], ['a', 'b'])` produce?

* **A)** `[1, 2, 'a', 'b']`
* **B)** `[(1, 'a'), (2, 'b')]` (as an iterator)
* **C)** `[[1, 'a'], [2, 'b']]`
* **D)** `{'1': 'a', '2': 'b'}`

**Answer: B**
**Explanation:** `zip` aggregates elements from each of the iterables into tuples.

---

### Question 43: Weak References

What is the purpose of the `weakref` module?

* **A)** To make code run faster
* **B)** To create references to objects that do not prevent them from being garbage collected
* **C)** To encrypt variables
* **D)** To handle small integers

**Answer: B**
**Explanation:** A weak reference is not enough to keep an object alive; if only weak references to an object remain, the garbage collector is free to destroy it.

---

### Question 44: Property Decorators

What is the advantage of using `@property`?

* **A)** It makes a method run faster
* **B)** It allows a method to be accessed like an attribute (getter) while maintaining encapsulation
* **C)** It makes an attribute private
* **D)** It is required for all class methods

**Answer: B**
**Explanation:** `@property` allows you to define a method that can be accessed like `obj.attr` instead of `obj.attr()`, often used for validation or computed values.

---

### Question 45: `collections.deque`

Why would you use a `deque` instead of a `list`?

* **A)** It uses less memory
* **B)** It is faster for  appends and pops from both the beginning and the end
* **C)** It sorts automatically
* **D)** It can only store integers

**Answer: B**
**Explanation:** While lists are  for inserting/removing at the beginning, `deque` (double-ended queue) handles these in .

---

### Question 46: `map()` Function

What is the result of `list(map(str, [1, 2, 3]))`?

* **A)** `[1, 2, 3]`
* **B)** `['1', '2', '3']`
* **C)** `"123"`
* **D)** `Error`

**Answer: B**
**Explanation:** `map()` applies the function (`str`) to every item in the iterable (`[1, 2, 3]`).

---

### Question 47: `__name__ == "__main__"`

What is the purpose of `if __name__ == "__main__":`?

* **A)** To define the main class of a file
* **B)** To ensure code only runs when the script is executed directly, not when imported as a module
* **C)** To start the Python debugger
* **D)** It is a required header for all Python files

**Answer: B**
**Explanation:** When a script is imported, `__name__` is set to the module's name. When run directly, it is set to `"__main__"`.

---

### Question 48: The `pass` Statement

What does the `pass` statement do?

* **A)** Breaks out of a loop
* **B)** Skips the current iteration of a loop
* **C)** It is a null operation; it does nothing and acts as a placeholder
* **D)** Returns a value from a function

**Answer: C**
**Explanation:** `pass` is used where syntactically a statement is required, but no action is needed (e.g., in an empty class or function).

---

### Question 49: Garbage Collection

How does Python primarily manage memory?

* **A)** Manual memory management (malloc/free)
* **B)** Reference counting and a cyclic garbage collector
* **C)** It doesn't; memory is cleared when the computer restarts
* **D)** Through the use of `global` keywords only

**Answer: B**
**Explanation:** Python uses reference counting to delete objects with zero references and a cycle detector to find groups of objects that reference each other but are unreachable.

---

### Question 50: `f-strings`

What is the correct syntax for an f-string in Python 3.6+?

* **A)** `f"Value is {val}"`
* **B)** `"Value is %f" % val`
* **C)** `"Value is {}".format(val)`
* **D)** `str("Value is " + val)`

**Answer: A**
**Explanation:** F-strings (formatted string literals) provide a concise and readable way to embed expressions inside string literals using curly braces.

---

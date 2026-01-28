# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging a buggy function
**My Prompt**
```
You are a senior Python developer tasked with debugging the following code snippet. The code below should calculate the sum of all of the even numbers in the list provided, but it is doing so incorrectly. Please fix the code so that it works as intended. Your response should be in the form of an organized code block.

def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed: check for even numbers
            total += num
    return total
```

## Problem 2: Refactoring an unreadable function
**My Prompt**
```
You are a senior Python developer tasked with cleaning up the following code snippet. The code below is logically correct, but could be refactored to be more clear, concise, and idiomatic. You may want to consider doing this by, for example, changing list comprehensions, iteration patterns, and variable names. Please clean up the following code and format your solution as an organized code block.

def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Return the names of users who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user["name"] for user in users if user["age"] >= 18]
```

## Problem 3: Documenting a function
**My Prompt**
```
You are a senior Python developer tasked with correctly documenting a function you have implemented. You must write a professional, NumPy-style docstring for the following function:

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

Note that the function raises a ValueError for invalid inputs. Please provide your function documentation formatted as a Python code block.
```

**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float or int
        The area of the rectangle, calculated as ``length * width``.

    Raises
    ------
    ValueError
        If either `length` or `width` is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(5, 3)
    15

    >>> calculate_area(2.5, 4)
    10.0

    >>> calculate_area(-1, 3)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
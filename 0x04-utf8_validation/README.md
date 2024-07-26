# UTF-8 Validation

This code provides a function `validUTF8` that checks if a given list of integers represents a valid UTF-8 encoding.

## Function Signature

```python
def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
```

## Algorithm

The `validUTF8` function iterates over the input list of integers and checks if each integer represents a valid UTF-8 character. It uses a byte count variable to keep track of the number of bytes expected for the current character.

The algorithm follows these steps:

1. Initialize the byte count to 0.
2. Iterate over each integer in the input list.
3. If the byte count is 0:
   - Check if the integer matches the pattern for a 2-byte or 3-byte character.
   - If it matches, update the byte count accordingly.
   - If it doesn't match, check if it represents a single-byte character or an invalid character and return False accordingly.
4. If the byte count is not 0:
   - Check if the integer matches the pattern for a continuation byte.
   - If it doesn't match, return False.
   - If it matches, decrement the byte count by 1.
5. After iterating over all the integers, check if the byte count is 0. If it is, return True; otherwise, return False.

This algorithm ensures that the input list represents a valid UTF-8 encoding.

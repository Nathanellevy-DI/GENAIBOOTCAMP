# Daily Challenge Code Explanation

This document breaks down how the `challenge.py` script works, step by step.

## 1. Getting the Input
```python
user_str = input("Please enter a string exactly 10 characters long: ")
```
* **What it does:** This line prompts the user to type something on their keyboard. Once they hit `Enter`, whatever they typed gets saved into a variable (like a storage box) named `user_str`. 

## 2. Checking the Length
```python
if len(user_str) < 10:
    print("String not long enough.")
elif len(user_str) > 10:
    print("String too long.")
else:
    print("Perfect string")
```
* **What it does:** The `len()` function is a built-in Python tool that counts how many characters are in the string. 
    * `if len(...) < 10`: If the length is strictly less than 10, it prints a warning.
    * `elif len(...) > 10`: `elif` stands for "else if". If the first check wasn't true, it checks if the length is strictly greater than 10.
    * `else:` This catches everything else. If it's not less than 10 and not greater than 10, it must be exactly 10!

## 3. Grabbing the First and Last Letters
```python
    print(f"First character: {user_str[0]}")
    print(f"Last character: {user_str[-1]}")
```
* **What it does:** These lines are indented under the `else:` statement, meaning they only run if the word is exactly 10 characters long.
    * `user_str[0]`: In programming, counting starts at 0. So `[0]` tells Python to grab the very first letter.
    * `user_str[-1]`: Using a negative number tells Python to count backward from the end. `[-1]` is a shortcut to always grab the very last letter.

## 4. Building the Word Step-by-Step
```python
    constructed_str = ""
    for char in user_str:
        constructed_str += char
        print(constructed_str)
```
* **What it does:** 
    * `constructed_str = ""`: This creates an empty text box (like a blank piece of paper) to hold our letters as we build them.
    * `for char in user_str:`: This is a **loop**. It tells Python to look at the word and go through it one single letter at a time. The current letter it is looking at is temporarily named `char`.
    * `constructed_str += char`: This adds the current letter (`char`) to whatever is already inside `constructed_str`.
    * `print(constructed_str)`: Finally, it prints out the currently built string.

**How the loop plays out for "hello":**
1. **Loop 1:** Looks at `h`. Adds `h` to the blank paper. Prints: `h`
2. **Loop 2:** Looks at `e`. Adds `e` to the paper (which already has `h`). Prints: `he`
3. **Loop 3:** Looks at `l`. Adds `l` to the paper. Prints: `hel`
4. ...and so on!

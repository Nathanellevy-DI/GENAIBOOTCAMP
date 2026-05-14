# 1. Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'}
print("--- Exercise 1 ---")
dict1 = {k: v for k, v in [("name", "Elie"), ("job", "Instructor")]}
print(dict1)

# 2. Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
print("\n--- Exercise 2 ---")
keys = ["CA", "NJ", "RI"]
values = ["California", "New Jersey", "Rhode Island"]
dict2 = {k: v for k, v in zip(keys, values)}
print(dict2)

# 3. Create a dictionary with the key as a vowel in the alphabet and the value as 0. (Do not use the fromkeys method).
print("\n--- Exercise 3 ---")
dict3 = {vowel: 0 for vowel in "aeiou"}
print(dict3)

# 4. Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet.
print("\n--- Exercise 4 ---")
dict4 = {i: chr(64 + i) for i in range(1, 27)}
import pprint
pprint.pprint(dict4)

# 5. Super Bonus: Given the string “awesome sauce” return a dictionary with the keys as vowels and the values as the count of vowels.
print("\n--- Super Bonus ---")
string = "awesome sauce"
bonus_dict = {vowel: string.count(vowel) for vowel in "aeiou"}
print(bonus_dict)

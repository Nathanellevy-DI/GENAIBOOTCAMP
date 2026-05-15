# 1. Given a list [1,2,3,4], print out all the values in the list.
print("--- Exercise 1 ---")
[print(val) for val in [1, 2, 3, 4]]

# 2. Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
print("\n--- Exercise 2 ---")
[print(val * 20) for val in [1, 2, 3, 4]]

# 3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).
print("\n--- Exercise 3 ---") 
res3 = [name[0] for name in ["El ie", "Tim", "Matt"]]
print(res3)

# 4. Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
print("\n--- Exercise 4 ---")
res4 = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(res4)

# 5. Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
print("\n--- Exercise 5 ---")
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
res5 = [num for num in list_a if num in list_b]
print(res5)

# 6. Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word reversed and in lower case (['eile', 'mit', 'ttam']).
print("\n--- Exercise 6 ---")
res6 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(res6)

# 7. Given two strings "first" and "third", return a new string (or list) with all the letters present in both words (["i", "r", "t"]).
print("\n--- Exercise 7 ---")
res7 = [char for char in "first" if char in "third"]
print(res7)

# 8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
print("\n--- Exercise 8 ---")
res8 = [num for num in range(1, 101) if num % 12 == 0]
print(res8)

# 9. Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
print("\n--- Exercise 9 ---")
res9 = [char for char in "amazing" if char not in "aeiou"]
print(res9)

# 10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
print("\n--- Exercise 10 ---")
res10 = [[i for i in range(3)] for j in range(3)]
print(res10)

# 11. Generate a 10x10 list with values 0-9
print("\n--- Exercise 11 ---")
res11 = [[i for i in range(10)] for j in range(10)]
import pprint
pprint.pprint(res11)

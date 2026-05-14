import math
import re

print(" Exercise 1 : Functions Exercises #1")

# difference
def difference(a, b):
    return a - b
print("difference(2,2):", difference(2,2)) # 0

# print_day
def print_day(n):
    days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    return days.get(n)
print("print_day(4):", print_day(4)) # Wednesday

# last_element
def last_element(lst):
    return lst[-1] if lst else None
print("last_element([1,2,3,4]):", last_element([1,2,3,4])) # 4

# number_compare
def number_compare(a, b):
    if a > b: return "First is greater"
    if b > a: return "Second is greater"
    return "Numbers are equal"
print("number_compare(1,2):", number_compare(1,2)) # Second is greater

# single_letter_count
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
print("single_letter_count('amazing','A'):", single_letter_count('amazing','A')) # 2

# multiple_letter_count
def multiple_letter_count(word):
    return {char: word.count(char) for char in word}
print("multiple_letter_count('hello'):", multiple_letter_count("hello")) # {'h':1, 'e':1, 'l':2, 'o':1}

# list_manipulation
def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        return lst.pop() if location == "end" else lst.pop(0)
    elif command == "add":
        if location == "end":
            lst.append(value)
        elif location == "beginning":
            lst.insert(0, value)
        return lst
print("list_manipulation([1,2,3], 'add', 'beginning', 20):", list_manipulation([1,2,3], "add", "beginning", 20)) # [20,1,2,3]

# is_palindrome
def is_palindrome(s):
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]
print("is_palindrome('tacocat'):", is_palindrome("tacocat")) # True
print("is_palindrome('a man a plan a canal Panama'):", is_palindrome("a man a plan a canal Panama")) # True

# frequency
def frequency(lst, search_term):
    return lst.count(search_term)
print("frequency([1,2,3,4,4,4], 4):", frequency([1,2,3,4,4,4], 4)) # 3

# flip_case
def flip_case(s, letter):
    return "".join([c.swapcase() if c.lower() == letter.lower() else c for c in s])
print("flip_case('Hardy har har', 'h'):", flip_case("Hardy har har", "h")) # "hardy Har Har"

# multiply_even_numbers
def multiply_even_numbers(lst):
    total = 1
    for x in lst:
        if x % 2 == 0: total *= x
    return total
print("multiply_even_numbers([2,3,4,5,6]):", multiply_even_numbers([2,3,4,5,6])) # 48

# mode
def mode(lst):
    return max(set(lst), key=lst.count)
print("mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]):", mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

# capitalize
def capitalize(s):
    return s[:1].upper() + s[1:]
print("capitalize('tim'):", capitalize("tim")) # Tim

# compact
def compact(lst):
    return [x for x in lst if x]
print("compact([0,1,2,'',[], False, {}, None, 'All done']):", compact([0,1,2,"",[], False, {}, None, "All done"])) # [1, 2, 'All done']

# partition
def partition(lst, callback):
    return [[x for x in lst if callback(x)], [x for x in lst if not callback(x)]]
def is_even(num): return num % 2 == 0
print("partition([1,2,3,4], is_even):", partition([1,2,3,4], is_even)) # [[2, 4], [1, 3]]

# intersection
def intersection(l1, l2):
    return [x for x in l1 if x in l2]
print("intersection([1,2,3], [2,3,4]):", intersection([1,2,3], [2,3,4])) # [2, 3]

# once
def once(func):
    def wrapper(*args, **kwargs):
        if wrapper.called: return None
        wrapper.called = True
        return func(*args, **kwargs)
    wrapper.called = False
    return wrapper

def add(a,b): return a + b
one_addition = once(add)
print("one_addition(2,2):", one_addition(2,2)) # 4
print("one_addition(2,2):", one_addition(2,2)) # None

# Super bonus
def run_once(func):
    def wrapper(*args, **kwargs):
        if wrapper.called: return None
        wrapper.called = True
        return func(*args, **kwargs)
    wrapper.called = False
    return wrapper

@run_once
def add_decorator(a,b): return a + b
print("add_decorator(2,2):", add_decorator(2,2)) # 4
print("add_decorator(2,20):", add_decorator(2,20)) # None

print("\n🌟 Exercise 2 : Functions Exercises#2 (Codewars)")

def solution(s):
    return s[::-1]

def new_avg(arr, newavg):
    val = math.ceil(newavg * (len(arr) + 1) - sum(arr))
    if val <= 0: raise ValueError("-")
    return val

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))

def max_diff(lst):
    return max(lst) - min(lst) if lst else 0

def count_smileys(arr):
    return len(list(filter(lambda x: re.match(r'^[:;][-~]?[)D]$', x), arr)))

def sentence_count(paragraph):
    return len(re.findall(r'[.?!]', paragraph)) if paragraph else 0

def race(v1, v2, g):
    if v1 >= v2: return None
    t = g * 3600 // (v2 - v1)
    return [t // 3600, (t % 3600) // 60, t % 60]

def shifted_diff(first, second):
    if len(first) != len(second): return -1
    return (second + second).find(first)

print("Codewars functions defined successfully.")

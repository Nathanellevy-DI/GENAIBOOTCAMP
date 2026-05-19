
user_str = input("Please enter a string exactly 10 characters long: ")

if len(user_str) < 10:
    print("String not long enough.")
elif len(user_str) > 10:
    print("String too long.")
else:
    print("Perfect string")
    
    # Print the first and last characters
    print(f"First character: {user_str[0]}")
    print(f"Last character: {user_str[-1]}")
    
    # Build the string character by character
    constructed_str = ""
    for char in user_str:
        constructed_str += char
        print(constructed_str)

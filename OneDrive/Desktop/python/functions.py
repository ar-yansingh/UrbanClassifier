def greet(first_Name, last_Name):
    print(f"Hi {first_Name} {last_Name}")
    print("welcome")


greet("Aryan", " Hamedani")
# TYPES OF FUNCTIONS
# 1-Perform a task
# 2- Return a value


def get_greeting(name):
    return f"HII{name}"


message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)

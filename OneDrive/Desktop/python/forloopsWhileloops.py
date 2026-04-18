for number in range(1, 4):
    print("At", number, number * ".")

for number in range(1, 10, 2):
    print("At", number, number * ".")

# while loops

command = ""
while command.lower() != " quit":
    command = input(">")
    print("ECHO", command)

# infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

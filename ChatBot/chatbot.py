print("Hello! My name is DICT_Bot.")
print("I was created in 2026.")
print("Please, remind me your name.")

name = input()
print(f"What a great name you have, {name}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {age}; that's a good time to start programming!")


print("Now I will prove to you that I can count to any number you want.")

number = int(input())

for i in range(number + 1):
    print(f"{i}!")

print("Let's test your programming knowledge.")
print("Why do we use methods?")

print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")


answer = int(input())

while answer != 2:
    print("Please, try again.")
    answer = int(input())

print("Congratulations, have a nice day!")
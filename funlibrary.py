import random

def increase(x):
    return x + 1


def count_to_ten():
    for i in range(1, 11):
        print(i)


def sum_list(x):
    total = 0
    for i in x:
        total += i
    return total


def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1 -1]
    return result


def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command

        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")


def mini(num_1, num_2, num_3):
    if num_1 <= num_2 and num_1 <= num_3:
        lowest = num_1
    elif num_2 <= num_1 and num_2 <= num_3:
        lowest = num_2
    else:
        lowest = num_3
    return lowest


def box(height, width):
    for i in range(height):
        print("o" * width)


def find(num_list, key):
    index = 0
    for item in num_list:
        index += 1
        if item == key:
            print("Found", key, "at position", index-1)


def fizzbuzz(endpoint):
    for i in range(1, endpoint+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fibonacci(length):
    x = 0
    y = 1
    print(f"{x:>27d}")
    print(f"{y:>27d}")
    for i in range(length):
        z = x + y
        print(f"{z:>27,d}")
        x = y
        y = z


def create_list(list_size):
    rand_list = []
    for i in range(list_size):
        rand_list.append(random.randint(1, 6))
    return rand_list


def count_list(lists, list_num):
    num = 0
    for item in lists:
        if item == list_num:
            num += 1
    return num


def average_list(lists):
    total = 0
    average = 0
    for item in lists:
        total += item
        average = total/len(lists)
    return average



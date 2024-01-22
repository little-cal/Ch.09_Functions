import random


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


def main():
    new_list = create_list(10000)
    for i in range(1, 7):
        count = count_list(new_list, i)
        print("There are", count, i, "'s")
    average = average_list(new_list)
    print("The average of all 10,000 numbers is:", average)


main()

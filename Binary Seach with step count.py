# Example of O(log n)

data_set = 100
your_number = 50


def binary_search(data_set, your_number):
    correct_num = data_set // 2
    steps = 1

    while correct_num != your_number:
        steps += 1
        diff = abs(correct_num - your_number) // 2 or 1

        if correct_num > your_number:
            correct_num -= diff
        elif correct_num < your_number:
            correct_num += diff

    return correct_num, steps


print(binary_search(data_set, your_number))

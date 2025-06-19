# Example of O(log n)

data_set = 100
your_number = 5

def binary_search(data_set, your_number):
    correct_num = data_set // 2
    
    while correct_num != your_number:
        diff = abs(correct_num - your_number) // 2 or 1
        
        if correct_num > your_number:
            correct_num -= diff
        elif correct_num < your_number:
            correct_num += diff
            
    return correct_num
    
print(binary_search(data_set, your_number))

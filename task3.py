numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def filter_numbers(x):
    if (x % 2) != 0 and x > 50:
        return True
    else:
        return False

print(list(filter(filter_numbers, numbers)))
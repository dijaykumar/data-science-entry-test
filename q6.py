def find_first_negative(lst):
# Task 1
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    
    return "No negatives"

# Task 2
print(find_first_negative([3, 5, -1, 7, -2, 8]))

print(find_first_negative([2, 10, 7, 0]))

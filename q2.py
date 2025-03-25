def find_and_replace(lst, find_val, replace_val):
# Task 1
    # Check if lst is a list
    if not isinstance(lst, list):
        return -1
    
    # Replace all occurrences of find_val with replace_val
    modified_lst = [replace_val if item == find_val else item for item in lst]
    
    return modified_lst

# Task 2
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

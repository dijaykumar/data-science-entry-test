def swap(x, y):
    # Swap the values of x and y
    x, y = y, x
    
    # Return -1 if x and y is not numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}")
    return

# Task 2
print(swap("Apple", 10))
print(swap(9, 17))

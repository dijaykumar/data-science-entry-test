def update_dictionary(dct, key, value):
# Task 1
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
    
    # Update or add the new key-value pair
    dct[key] = value  
    return dct

# Task 2
dct1 = {}
print(update_dictionary(dct1, "name", "Alice"))

dct2 = {"age": 25}
print(update_dictionary(dct2, "age", 26))

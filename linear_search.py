def linear_search(data_list, target_item):
    """
    Performs a linear search to find a target_item in a data_list.

    Args:
        data_list (list): The list of items to search through.
        target_item: The item we are looking for.

    Returns:
        int: The index (position) of the target_item if found,
             otherwise returns -1 (a common way to indicate "not found").
    """

    # We use 'enumerate' to get both the index (position) and the value
    # of each item as we go through the list.
    # 'index' will be 0, 1, 2, ...
    # 'current_item' will be the actual value at that index.
    for index, current_item in enumerate(data_list):
        # STEP 1: Look at the current item.
        print(f"Checking index {index}: Is '{current_item}' equal to '{target_item}'?")

        # STEP 2: Compare the current item with what we are looking for.
        if current_item == target_item:
            # STEP 3: If they match, we found it!
            print(f"  SUCCESS! Found '{target_item}' at index {index}.")
            return index  # Return the position (index) and stop the function.

        # If they don't match, the loop automatically moves to the next item
        # because we are using 'for ... in ...'.

    # STEP 6: If the loop finishes without finding the item (meaning 'return index'
    # was never called), it means the target was not in the list.
    print(f"  FAILURE! '{target_item}' not found in the list.")
    return -1  # Indicate that the item was not found.

# --- Practical Examples ---
print("--- Linear Search Examples ---")

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]

# Example 1: Item is found
item_to_find_1 = "Keyboard"
print(f"\nSearching for '{item_to_find_1}' in {products}")
result_index_1 = linear_search(products, item_to_find_1)
if result_index_1 != -1:
    print(f"'{item_to_find_1}' is at position (index) {result_index_1}.")
else:
    print(f"'{item_to_find_1}' was not found.")

# Example 2: Item is found at the beginning
item_to_find_2 = "Laptop"
print(f"\nSearching for '{item_to_find_2}' in {products}")
result_index_2 = linear_search(products, item_to_find_2)
if result_index_2 != -1:
    print(f"'{item_to_find_2}' is at position (index) {result_index_2}.")
else:
    print(f"'{item_to_find_2}' was not found.")

# Example 3: Item is NOT found
item_to_find_3 = "Printer"
print(f"\nSearching for '{item_to_find_3}' in {products}")
result_index_3 = linear_search(products, item_to_find_3)
if result_index_3 != -1:
    print(f"'{item_to_find_3}' is at position (index) {result_index_3}.")
else:
    print(f"'{item_to_find_3}' was not found.")

# Example 4: Searching numbers
prices = [10, 25, 5, 80, 15]
price_to_find = 25
print(f"\nSearching for '{price_to_find}' in {prices}")
result_index_4 = linear_search(prices, price_to_find)
if result_index_4 != -1:
    print(f"'{price_to_find}' is at position (index) {result_index_4}.")
else:
    print(f"'{price_to_find}' was not found.")
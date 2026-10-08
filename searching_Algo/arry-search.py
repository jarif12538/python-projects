def arrySearch(arr, target):
    """
    This function searches for a target value in a given array.
    
    Parameters:
    arr (list): The array to search through.
    target: The value to search for in the array.
    
    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
arr = list(map(int, input("Enter numbers separated by space: ").strip().split()))
target = int(input("Enter the target number to search for: "))
result = arrySearch(arr, target)
if result != -1:
    print(f"Target found at index: {result}")
else:   
    print("Target not found in the array.") 
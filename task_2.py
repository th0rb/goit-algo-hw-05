def upper_bound_binary_search(arr: list, target : float) -> tuple:
    low = 0 
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        iterations += 1

        if guess == target:
            return iterations, guess
        elif guess > target:
            upper_bound = guess
            high = mid - 1
        else:
            low = mid + 1
    
    return iterations, upper_bound

# Тести:
arr = [1.1, 1.5, 2.6, 3.8, 4.6]
print(upper_bound_binary_search(arr, 2.7))  # Виведе: (2, 3.8)
print(upper_bound_binary_search(arr, 4))  # Виведе: (3, 4.6)
print(upper_bound_binary_search(arr, 6.0))  # Виведе: (3, None)
print(upper_bound_binary_search(arr, 2.6))  # Виведе: (1, 2.6)
print(upper_bound_binary_search(arr, 0))  # Виведе: (2, 1.1)

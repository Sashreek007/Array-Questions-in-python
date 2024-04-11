def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        else:
            seen.add(num)  # Add the element to the set
    return False  # No duplicates found

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
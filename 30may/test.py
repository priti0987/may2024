def ArrayChallenge(arr):
    def can_sum_to_target(nums, target, index):
        print("nums",nums)
        print("target",target)
        print("index",index)
        if target == 0:
            return True
        if target < 0 or index < 0:
            return False
        # Recursively check two possibilities: including the current number or not
        print(can_sum_to_target(nums, target - nums[index], index - 1))
        print(can_sum_to_target(nums, target, index - 1))
        return can_sum_to_target(nums, target - nums[index], index - 1) or can_sum_to_target(nums, target, index - 1)

    if len(arr) < 2:
        return "false"

    # Identify the largest number
    largest = max(arr)
    arr.remove(largest)

    # Check if any subset of the remaining numbers can sum to the largest number
    if can_sum_to_target(arr, largest, len(arr) - 1):
        return "true"
    else:
        return "false"


# Example usage:
arr = [4, 6, 23, 10, 1, 3 ]
#print(arr,ArrayChallenge(arr))  # Output should be "true"
print(ArrayChallenge([1, 2, 3, 9,10]))  # Output should be "false"

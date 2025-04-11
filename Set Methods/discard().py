nums = {1, 2, 3}
nums.discard(3)
print(nums)  # Output: {1, 2}

nums.discard(5)  # ✅ No error, just does nothing
print(nums)      # Output: {1, 2}

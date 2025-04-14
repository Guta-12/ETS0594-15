nums = [3, 1, 4, 2]
nums.sort()
print(nums) 
nums.sort(reverse=True)
print(nums) 
 # Output: [1, 2, 3, 4]
 # Output: [4, 3, 2, 1]
words = ['banana', 'apple', 'kiwi']
words.sort(key=len)
print(words)  # Output: ['kiwi', 'apple', 'banana']

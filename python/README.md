The  method in Python is part of the string class, and its primary purpose is to check if all the alphabetic characters in a string are uppercase. It is frequently used in text processing when determining whether a string satisfies certain case-related conditions. 
Return Value: A boolean value:
Returns True if all the alphabetic characters in the string are uppercase
Returns False otherwise.
Non-Alphabetic Characters: Numbers, spaces, symbols, and punctuation are ignored when determining the result.

# str.lower()
-Converts all characters in the string to lowercase.
-It does not change numbers or special characters.
-Useful when you need case-insensitive comparisons, such as checking if user input matches a stored value.
# str.title()
-Capitalizes the first letter of each word and converts the rest to lowercase.
-It treats non-alphabetic characters (like spaces, hyphens) as word boundaries.
-Often used for names or titles formatting.
Note: title() doesn’t always work well for words with mixed capitalization like "McDonald's" or "iPhone" (it would output "Mcdonald'S" or "Iphone")
# str.capitalize()
-Capitalizes only the first letter of the entire string.
-The rest of the string is converted to lowercase.
-Good for formatting sentences to start with a capital letter.
# str.swapcase() 
is a string method that returns a new string with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase.
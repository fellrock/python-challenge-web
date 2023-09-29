def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:  # If the character is a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():  # If the character is an opening bracket
            stack.append(char)

    return not stack  # Return True if the stack is empty, False otherwise

# Test the function
print(is_valid("{[12e21]}"))  # Returns: True
print(is_valid("{(]())"))  # Returns: False
print(is_valid("{([asdad)]}"))  # Returns: False

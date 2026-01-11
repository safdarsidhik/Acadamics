# Check if parentheses string is valid.

# Answer: Use stack and matching pairs.

# Test: "([])" → True, "(]" → False

Test = "([)"

mapping = {')': '(', '}': '{', ']': '['}
stack = []

def isValid(self, s):
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack   
print(isValid(None, Test))
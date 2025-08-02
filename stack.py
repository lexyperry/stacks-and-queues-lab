def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching.values(): 
            stack.append(char)
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return not stack 

print(is_valid_parentheses("()"))         # True
print(is_valid_parentheses("([{}])"))     # True
print(is_valid_parentheses("{[()]}[]"))   # True
print(is_valid_parentheses("{[(])}"))     # False
print(is_valid_parentheses("((("))        # False

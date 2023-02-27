def equal_braces(s):
    """
    Returns True if the given string has equal number of opening and closing braces,
    otherwise returns False.
    """
    stack = []
    
    for c in s:
        n=len(stack)
        if c == '(':
            stack.append(c)
        elif c == '{':
            stack.append(c)
        elif c == '[':
            stack.append(c)
            
        if c == ')' and stack[n-1]=='(':
            stack.pop()
        if c == '}' and stack[n-1]=='{':
            stack.pop()
        
        if c == ']' and stack[n-1]=='[':
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False



s=input("Enter the expression:")
print(equal_braces(s))
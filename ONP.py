# cook your dish here
def solution(expression):
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = []
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char in '+-*/^':
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ''.join(output)


if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        expression = input()
        print(solution(expression))
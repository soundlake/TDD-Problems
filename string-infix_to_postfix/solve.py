import re

def infix_to_postfix(infix):
    stack = []
    result = []

    for i in re.finditer('\d+|[\+\-\*\/\(\)]', infix):
        t = i.group(0)
        print(t, stack, result)
        if t == '(':
            stack.append(t)
        elif t == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        elif t in '+-*/':
            if stack and stack[-1] != '(':
                if not (t in '*/' and stack[-1] in '+-'):
                    result.append(stack.pop())
            stack.append(t)
        elif re.match('\d+', t):
            result.append(t)

    stack.reverse()
    return ' '.join(result + stack)

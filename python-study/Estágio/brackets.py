import sys
import math

expression = input()
brackets = []
i = 0
while i != len(expression):
    if expression[i] in '([{':
        brackets.append(expression[i])
    else:
        if expression[i] == ')':
            if i == 0:
                print('false')
                break
            elif brackets[-1] != '(':
                print('false')
                brackets.pop()
                break
        elif expression[i] == ']':
            if i == 0:
                print('false')
                break
            elif brackets[-1] != ']':
                print('false')
                brackets.pop()
                break
        elif expression[i] == '}':
            if i == 0:
                print('false')
                break
            elif brackets[-1] != '}':
                print('false')
                brackets.pop()
                break
    i+=1


if i == 0:
    print('true')
else:
    print('false')
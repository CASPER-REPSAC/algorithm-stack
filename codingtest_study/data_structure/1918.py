import sys 


stack = []
result = ""

fm = input()

for i in range(len(fm)):
    if fm[i] == '(' :
       stack.append(fm[i])
    elif fm[i] == ')' :
        top = stack.pop()
        while top != '(':
            result += top
            top = stack.pop()
    elif fm[i] == '+' or fm[i] == '-':
        if stack != []:
            top = stack.pop()
            while top != '(' and stack != []:
                result += top
                top = stack.pop()
            stack.append(top)
            stack.append(fm[i])
        else :
            stack.append(fm[i])
    elif fm[i] == '*' or fm[i]=='/' :
        if stack != []:
            top = stack.pop()
            while (top == '*' or top == '/') and stack != []:
                result += top
                top = stack.pop()
            stack.append(top)
            stack.append(fm[i])
        else :
            stack.append(fm[i])
    else :
        result += fm[i]

while stack != []:
    result+= stack.pop()

print (result)
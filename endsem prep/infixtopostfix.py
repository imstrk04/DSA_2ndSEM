output = [] 
operator = []
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^':3}
exp = input("Enter infix expression: ")
for ch in exp:
    if ch == '(':
        operator.append(ch)

        
    elif ch == ')':
        while (operator[-1] != '('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif ch == '^' or ch == '*' or ch == '/' or ch == '+' or ch == '-':
        if len(operator) != 0:
            while (priority[operator[-1]]>= priority[ch]):
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    else:
        output.append(ch)
while (len(operator) != 0):
    ele = operator.pop()
    output.append(ele)

print("Infix exp:", exp)
print("Postfix exp:", end = " ")
for ele in output:
    print(ele, end = '')
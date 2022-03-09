# 定义优先级
def precede(op1, op2):
    dic = {'(': 2, ')': 2, '*': 1, '/': 1, '+': 0, '-': 0}
    if dic[op2] > dic[op1]:
        return True
    else:
        return False

# 运算符定义
def operate(n1, op, n2):
    num1 = int(n1)
    num2 = int(n2)
    ans = 0
    if op == '-':
        ans = num1 - num2
    elif op == '+':
        ans = num1 + num2
    elif op == '*':
        ans = num1 * num2
    elif op == '/':
        ans = int(num1 / num2)
    return ans

# 中缀表达式转后缀表达式
def trans(str):
    newStr = ''
    stack = []
    for s in str:
        if ord('0') <= ord(s) <= ord('9'):
               newStr += s
        elif s == '(':
            stack.append(s)
        elif s == ')':
            for i in range(len(stack)-1, -1, -1):
                if stack[i] != '(':
                    newStr += stack.pop()
                else:
                    stack.pop()
                    break
        else:
            for i in range(len(stack)-1, -1, -1):
                if stack[i] == '(':
                    break
                elif not precede(stack[i], s):
                    newStr += stack.pop()
            stack.append(s)
    for i in range(len(stack) - 1, -1, -1):
        newStr += stack.pop()
    return newStr

# 后缀表达式计算
def caculate(str):
    tokens = trans(str)
    if len(tokens) == 1:
        return int(tokens)
    stack = []
    for i, x in enumerate(tokens):
        if x not in '+-*/':
            stack.append(x)
        else:
            a = stack.pop()
            b = stack.pop()
            res = operate(b, x, a)
            if i != len(tokens) - 1:
                stack.append(res)
            else:
                return res

print(caculate('9+(3-1)*3+1/2'))

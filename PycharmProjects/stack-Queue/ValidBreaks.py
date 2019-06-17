from Arraystack import ArrayStack

def isValid(s):
    mystack = ArrayStack()
    for i in s:
        if i in '([{':
            mystack.push(i)
            continue
        else:
            if mystack.isEmpty():
                return False
        tope = mystack.pop()
        if i == ')' and tope != '(':
            return False
        if i == ']' and tope != '[':
            return False
        if i == '}' and tope != '{':
            return False
    return mystack.isEmpty()

print(isValid('[]{}'))
print(isValid('[]{'))


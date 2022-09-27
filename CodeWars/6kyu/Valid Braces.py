def valid_braces(string):
    braces = {'[':']',
              '{':'}',
              '(':')'
             }
    stack = []
    for i in string:
        for key,value in braces.items():
            if i == key:
                stack.append(i)
            elif i == value and stack != []:
                if stack[len(stack)-1] == key:
                    stack.pop()
                else:
                    return False
            elif i == value and stack == []:
                return False
    if stack == []:
        return True
    else:
        return False
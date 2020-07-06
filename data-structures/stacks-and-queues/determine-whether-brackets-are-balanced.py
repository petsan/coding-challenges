brackets = "([{}])"

bracketsUnbalanced = "([[{}])"

def balance(s):
    stack = []
    print(s)
    for char in s:
        if char in [ "(", "[", "{"] :
            stack.append(char)
            print(stack)
        else:
            # check character is not unmatched
            if not stack:
                return False
            
            # Char is a closing bracket. Check top of stack if it matches.
            if (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()
            print(stack)

    return len(stack) == 0

balance(brackets)

balance(bracketsUnbalanced)
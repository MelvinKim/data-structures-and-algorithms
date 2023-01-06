def isValid(s):
    if s == "" or s == None:
        return False
    
    stack = []
    closeToOpenMap = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    for ch in s:
        if ch in closeToOpenMap:
            if stack and stack[-1] == closeToOpenMap[ch]:
                stack.pop()
            else:
                return False    
        else:
            stack.append(ch)
            
    return True if not stack else False

print("isValid: ", isValid("([)]"))


""" 
1: Create stack data structure
2: Traverse each charater in input string
3: Check if the type of open parentheses is of (, [, { and push it to stack.
4: Check if the type of parentheses is closed ) && check if the    last pushed element in the stack is open ( 
then pop that open parentheses from the stack since parentheses are     valid.  (Since current parentheses is closed and last pushed is open, that means we have continous open and closed parentheses)
5:  Check if the type of parentheses is closed ] && check if the    last pushed element in the stack is open [
then pop that parentheses from the stack since parentheses are     valid.
6:  Check if the type of parentheses is closed } && check if the    last pushed element in the stack is open {
then pop that parentheses from the stack since parentheses are     valid.
7: Return if stack is empty( stack will be empty when all the open brackets that pushed in stack have find closed bracket, if its not then stack will not be empty).
"""
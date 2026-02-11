def transform(self, s):
    # The generated postfix expression of s
    output = []
    # Wrap `s` with \'(\' and \')\' to make processing easier
    s = s + \')\'
    stack = [\'(\']
    prevC = \'(\'

    hasNum = False
    num = 0
    for c in s:
        if c == \' \':
            continue

        # c is part of number
        if c.isdigit():
            hasNum = True
            num = num * 10 + int(c)
            prevC = c
            continue
        # c is operator
        if hasNum:
            hasNum = False
            output.append(num)
            num = 0

        # check if is negative unary operator
        if c == \'-\' and (prevC == \'(\' or prevC in self.operators):
            c = \'neg\'
        
        # Pop until \'(\'
        while self.precedence_stack[stack[-1]] >= self.precedence_input[c]:
            popped = stack.pop()
            if popped != \'(\':
                output.append(popped)
            else:
                break
        # push input on to the stack
        if c != \')\':
            stack.append(c)

        prevC = c
    
    return output
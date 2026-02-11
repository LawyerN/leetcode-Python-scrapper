class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
                \'+\' : lambda x, y : x + y,
                \'-\' : lambda x, y : x - y,
                \'*\' : lambda x, y : x * y,
                \'/\' : lambda x, y : int(x / y)
             }

        stack = []
        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()
                stack.append(op[i](a, b))
            else:
                stack.append(int(i))
                
        return stack.pop()
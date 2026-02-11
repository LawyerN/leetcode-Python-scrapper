from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if token == "+":
                    result = left_operand + right_operand
                elif token == "-":
                    result = left_operand - right_operand
                elif token == "*":
                    result = left_operand * right_operand
                else:
                    result = int(left_operand / right_operand)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
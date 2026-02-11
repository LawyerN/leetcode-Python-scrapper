def recursive(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.recursive(p.left, q.left) and self.recursive(p.right, q.right)
        
    def iterative(self, p, q):
        stack = [(p, q)]
        while len(stack):
            first, second = stack.pop()
            if not first and not second: pass
            elif not first or not second: return False
            else:
                if first.val != second.val: return False
                stack.append((first.left, second.left))
                stack.append((first.right, second.right))
        return True
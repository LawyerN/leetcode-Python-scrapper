def ff(n):
            if n in (None, p, q): return n
            l, r = ff(n.left), ff(n.right)
            if l and r: return n
            return l or r
        return ff(root)
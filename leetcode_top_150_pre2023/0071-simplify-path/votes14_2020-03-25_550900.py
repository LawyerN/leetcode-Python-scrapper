class Solution1:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i<len(path):
            while i< len(path) and path[i]==\'/\':
                i+=1
            start = i
            while i< len(path) and path[i]!=\'/\':
                i+=1
            strr = path[start:i]
            if strr == \'..\':
                if stack:
                    stack.pop()
            elif strr and strr != \'.\' :
                    stack.append(strr)
        if not stack:
            return \'/\'
        return \'/\' + \'/\'.join(stack)
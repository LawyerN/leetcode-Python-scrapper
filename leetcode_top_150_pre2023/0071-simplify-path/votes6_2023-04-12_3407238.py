class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # different directories present in the string
        temp = path.split(\'/\') 

        for i in temp:
            if i != \'.\' and i != \'\' and i != \'..\':
                stack.append(i) # add if it is directory

            # move to back directory if \'..\'
            elif i == \'..\':
                if stack:
                    stack.pop()
        
        return \'/\' + \'/\'.join(stack)
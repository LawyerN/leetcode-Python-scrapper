L = {\'2\':"abc",\'3\':"def",\'4\':"ghi",\'5\':"jkl",
     \'6\':"mno",\'7\':"pqrs",\'8\':"tuv",\'9\':"wxyz"}

class Solution:
    def letterCombinations(self, D: str) -> List[str]:
        lenD, ans = len(D), []
        if D == "": return []
        def dfs(pos: int, st: str):
            if pos == lenD: ans.append(st)
            else:
                letters = L[D[pos]]
                for letter in letters:
                    dfs(pos+1,st+letter)
        dfs(0,"")
        return ans
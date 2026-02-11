class Solution:
    def coinChange(self, C: List[int], A: int) -> int:
        C.sort()
        ans = 10001
        def rc(amt, num, cix):
            nonlocal ans
            if amt == 0:
                if num < ans: ans = num
            elif amt > 0 and ~cix:
                n = ceil(amt / C[cix])
                if num + n >= ans: return
                for i in range(n, -1, -1):
                    rc(amt - i * C[cix], num + i, cix - 1)
        rc(A, 0, len(C)-1)
        return ans if ans < 10001 else -1
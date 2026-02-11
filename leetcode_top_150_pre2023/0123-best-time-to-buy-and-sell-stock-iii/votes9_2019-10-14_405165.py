class Solution(object):
    def maxProfit(self, prices):
        # dynamic programming
        fb, fs, sb, ss = float(\'inf\'), 0, float(\'inf\'), 0
        for price in prices:
            fb = min(fb, price)  # keep minimal
            fs = max(fs, price-fb)  # maximum if one transaction
            sb = min(sb, price-fs)  # total drop volume level
            ss = max(ss, price-sb)  # maximum if sum of two transactions
        return ss
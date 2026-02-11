def using_inbuilt_counter(self, n):
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)
    
    def using_bit_manipulation(self, n):
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        return count
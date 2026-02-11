class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  # set to keep track of visited numbers
        
        while n != 1:  # continue loop until happy or stuck in cycle
            sum_of_squares = 0
            
            # compute sum of squares of digits in n
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n //= 10
            
            # check if sum is already visited
            if sum_of_squares in visited:
                return False
            
            # add sum to visited set
            visited.add(sum_of_squares)
            
            # set n to be the sum of squares for next iteration
            n = sum_of_squares
        
        return True
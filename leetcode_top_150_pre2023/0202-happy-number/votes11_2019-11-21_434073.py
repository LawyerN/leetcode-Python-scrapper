# We use a set to store the sume of squares at each step. Don\'t use a list, 
        # because checking values in list takes O(n), but it takes O(1) for set.
        n_set = set()
        sqr = 0  
        while sqr != 1:
            sqr = 0  #This variable is set to zero at the beginning of each iteration.
			
            #This loop calculates the sum of the squares of digits in n:
            while n > 0: 
                sqr += (n % 10) ** 2
                n = n // 10
				
            #If the number is happy, the sum of squares will be equal to 1, after a few iterations.
            if sqr == 1: return True
			
            #If the number is not happy, at some point, the sum of squares will be repeated in a cycle, 
			# meaning the code will repeat the same calculations over and over in an infinite loop. 
			# So, we check if sqr has happened before:
            elif sqr in n_set: return False
            else: 
                n = sqr       # repeat the process, but the new n will be equal to sum of the squares.
                n_set.add(n)  # add the new n to the set in order to keep a record of sum of the squares.
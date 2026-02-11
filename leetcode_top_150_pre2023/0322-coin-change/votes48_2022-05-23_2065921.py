def coinChange(self, coins: List[int], amount: int) -> int:
        
		# queue with current amount and number of coins
        q = deque([(amount,0)])
		
		# set with visited amount to avoid duplicate work
        visited = set()
        
        while q:
            cur, n_coins = q.popleft()
			
			# if current amount is equal to zero we have found the answer
            if cur == 0:
                return n_coins
            
            for c in coins:
                new_cur = cur - c
				
				# if we\'ve already checked this amount or amount gone below zero there is no need
				# to continue search this path
                if new_cur in visited or new_cur < 0:
                    continue
				
				# continue search the path and mark new amount as visited
                q.append((new_cur,n_coins+1))
                visited.add(new_cur)
                    
        return -1
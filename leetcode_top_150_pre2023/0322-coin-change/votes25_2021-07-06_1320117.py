def coinChange(coins, amount):

	if amount == 0:
		return 0
	from collections import deque
	q = deque()
	q.append(amount) # amt, depth
	visited = set()
	depth = 0
	while q:
		for i in range(len(q)):
			amt = q.popleft()

			if amt < 0: # skip prune branches that yeild -ve nodes
				continue

			elif amt == 0:
				return depth

			if amt not in visited: # skip nodes seen before - see explanantion above
				visited.add(amt)

				# move down a level
				for c in coins: 
					q.append(amt-c)

		depth += 1

	return -1
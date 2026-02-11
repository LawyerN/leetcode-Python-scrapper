# Approach 1 using a visited hash_set
        # Time -O(n), Space- O(n)
node_set = set()
while(head):
	if head in node_set:
		return True
	node_set.add(head)
	head = head.next
return False
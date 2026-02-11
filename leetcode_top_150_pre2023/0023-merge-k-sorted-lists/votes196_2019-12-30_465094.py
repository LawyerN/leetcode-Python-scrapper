def mergeKLists_Python2(self, lists):
	h = []
	head = tail = ListNode(0)
	for i in lists:
		if i:
			heapq.heappush(h, (i.val, i))

	while h:
		node = heapq.heappop(h)[1]
		tail.next = node
		tail = tail.next
		if node.next:
			heapq.heappush(h, (node.next.val, node.next))

	return head.next
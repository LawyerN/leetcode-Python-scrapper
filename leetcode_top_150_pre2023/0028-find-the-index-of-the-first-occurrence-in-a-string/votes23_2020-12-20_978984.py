def strStr(self, haystack: str, needle: str) -> int:
	if needle == \'\': return 0
	N = len(needle)
	base = 26  # base of the polynomial hash
	prime_mod = 101  # to avoid hash overflow, doesn\'t have to be prime number

	def charcode(ch):
		return ord(ch) - ord(\'a\')

	def myhash(s):
		\'\'\'polynomial hash of a string\'\'\'
		my_hash = 0
		for ch in s:
			my_hash = (charcode(ch) + my_hash * base) % prime_mod
		return my_hash

	needle_hash = myhash(needle)
	rolling_hash = myhash(haystack[:N-1])

	first_pow = base ** (N-1)  # the first digit\'s base as a const, to avoid recomputation

	for i in range(N-1, len(haystack)):
		rolling_hash = (rolling_hash * base + charcode(haystack[i])) % prime_mod
		if rolling_hash == needle_hash and needle == haystack[i+1-N:i+1]: return i+1-N
		rolling_hash = (rolling_hash - charcode(haystack[i+1-N]) * first_pow) % prime_mod

	return -1
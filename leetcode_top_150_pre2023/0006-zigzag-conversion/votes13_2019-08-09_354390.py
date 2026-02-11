s = "PAYPALISHIRING"
numRow = 3
        """
        p (0)      a(4)      h(8)         n(12)
        a (1) p(3) l(5) s(7) i(9) i(11)  g(13)
        y (2)      i(6)      r(10)
        """
# There is a pattern consists 4 elements as below:
		"""
        p (0)     
        a (1)  p(3) 
        y (2)     
        """
# The ith element can be mapping into this pattern by i%pattern_length:
The first line: 0 % 4 = 4 % 4 = 8 % 4 = 12 % 4 =0
"""
 p (0)      a(4)      h(8)         n(12)
"""
The second line: there is 2 type pattern:
a: 1 % 4 = 5 % 4 = 9 % 4 = 13 % 4 = 1
b: 3 % 4 = 7 % 4 = 11 % 4 = 3
So here we need an extra mapping to deal with these 2 situations.
1 = 4 - 3 is key to combine these two situation into one.
 d={i:i if i<numRows else (period-i) for i in range(period)}
"""
a (1) p(3) l(5) s(7) i(9) i(11)  g(13)
"""
The third line:
2 % 4 = 6 % 4 = 10  % 4 = 2
"""
 y (2)      i(6)      r(10)
"""
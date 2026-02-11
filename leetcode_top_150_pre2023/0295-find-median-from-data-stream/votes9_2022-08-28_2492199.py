add 3
=====
step one:
---------
first_half: [-3] (we must multiply by -1 for Python\'s max-heap)
second_half: []

step two
--------
first_half: []
second_half: [3] (first_half current stores negative number. hence, we must multiply it by -1 again)

step three
----------
first_half: [-3] (first_half\'s length is less than second_half. hence, we must push the number back to it)
second_half: []

add 5
=====
step one:
---------
first_half: [-5, -3] (we must multiply by -1 for Python\'s max-heap)
second_half: []

step two
--------
first_half: [-3]
second_half: [5] (first_half current stores negative number. hence, we must multiply it by -1 again)

step three
----------
first_half: [-3]
second_half: [5] (we keep as is b/c first_half\'s size == second_half\'s size)
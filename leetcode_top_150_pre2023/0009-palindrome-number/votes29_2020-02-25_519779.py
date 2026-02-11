def isPalindrome(self, num):
	#negatives can\'t be palindromes cause of their minus sign so
	#instead of dealing with this in our main code, we get rid of this possibility immediately
    if num < 0: return False

    """
	Steps in this algorithm:
    1. get the reversed number (the original number but its digits reversed). e.g. 125 becomes 521
    2. if the reversed number == original number, its a palindrome! Done!
    
	How to get reversed number (rev_num):
    1. we do this by \'popping\' the num\'s last digit. e.g. 125 becomes 12, we store 5 as last_digit
    2. and then \'appending\' that last digit to rev_num. e.g. rev_num starts at 0. 0 becomes 5 after appending 5. 5 becomes 52 after appending 2 
    3. we keep doing this until all num\'s digits have been popped, which happens when num becomes 0. e.g. when num is 0, rev_num will be 521
	Note: the \'popping\' and \'appending\' is done with cute math tricks, which is more space saving & usually faster than converting the number to a string
	"""
	
    original_num = num
    rev_num = 0
	#each line inside the while loop below does a neat math trick, try them w/ pencil & paper to understand why they work
    while num > 0:
	  #get last digit from num. e.g. 125 % 10 returns 5
      last_digit = num % 10
	  #remove last digit from num. e.g. lets say num is 125. num is then set to 125 // 10 which is 12
      num = num // 10
	  #effectively, the above two lines of code have simply popped the last digit from num and saved it. e.g. num is changed from 125 to 12. last_digit is set to 5

      #append last digit to right of rev_num, e.g. 5 becomes 52 after appending 2
      rev_num = rev_num*10 + last_digit
    
	#once the while loop is done, rev_num represents the reversed number of the original number
	#in below code, if they match, its a palindrome, since palindromes are symmetrical! e.g. 125 does not equal 521 so this condition would fail
    return original_num == rev_num
	
	"""
	side note: the while loop gets completely skipped if num is initially 0.
	Here that situation conviently still gives us the right answer as rev_num will be 0 so its no problem, but
	still its good to think about edge cases.
	"""
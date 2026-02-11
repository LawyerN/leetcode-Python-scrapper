Given : val = 2
1 2 2 2 5 2 5 
i           j
First Start from the far end 
1 2 2 2 5 2 5 
  i         j
when nums[i] == val , nums[i] = nums[j]
1 2 2 2 5 2 5 
    i     j 
if(num[j]) is also val then move it left till its not
1 5 5 2 2 2 5 
    i   j  
when i==j.. stop
1 5 5  2  2 2 5 
      i,j
you see that i can still be val, 
so we check before returning the answer
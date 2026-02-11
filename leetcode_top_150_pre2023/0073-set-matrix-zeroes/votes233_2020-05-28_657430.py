**Most optimized using O(1) space:** But, we can do even better, O(1) - initial ask of the problem. What if instead of having a separate array to track the zeroes, we simply use the first row or col to track them and then go back to update the first row and col with zeroes after we\'re done replacing it? The approach to get constant space is to use first row and first col of the matrix as a tracker. 
* At each row or col, if you see a zero, then mark the first row or first col as zero with the current row and col. 
* Then iterate through the array again to see where the first row and col were marked as zero and then set that row/col as 0. 
* After doing that, you\'ll need to traverse through the first row and/or first col if there were any zeroes there to begin with and set everything to be equal to 0 in the first row and/or first col. 

Time complexity for all three progression is O(m * n).



**Space:** O(1) for modification in place and using the first row and first col to keep track of zeros instead of zeroes_row and zeroes_col
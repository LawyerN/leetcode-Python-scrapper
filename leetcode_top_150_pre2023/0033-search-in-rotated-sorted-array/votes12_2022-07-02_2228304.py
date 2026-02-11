* the rotated array has **two sorted** parts
	* Part 1: 
		* nums[i] <= nums[n-1]
		* i.e. : 1,2,3,4
		
	* Part 2:
		* nums[i] > nums[n-1]
		*  i.e. : 5,6,7

* Understand that if we somehow we know the index of the element that seprates the two parts (Pivot) then we will have an idea about - in which part our target element is present
	* In the given example, firstly we need to find the index of \'7\' which is the pivot element

### **How to find the index of Pivot element?**

* We will use the same property that defined Part1 and Part2 to find the pivot index
* Reminder 
	* "Pivot is in Part2"
	* the unique property of pivot is that, the pivot element is greater than next index element ( 7 > 1)
		* **nums[idx] > nums[idx+1]** (idx = index of pivot)
		
* As we want optimized approach so we will use binary search to find the pivot index
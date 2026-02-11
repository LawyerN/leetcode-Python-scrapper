class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        list1=[]
        for i,n in enumerate(numbers):
            left,right=i+1,len(numbers)-1
            while left<=right:
                mid=(left+right)//2
                if (numbers[mid]+n)==target:
                    return i+1,mid+1
                if (numbers[mid]+n)<target:
                    left=mid+1
                else:
                    right=mid-1
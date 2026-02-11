class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """


        # start a pointer at 0 called start
        # start a pointer at 0 called end
        # start a variable called length
        # you start at the beginning of the list and sum. if the sum at any time is less than 0, you subtract from the start. and move the pointer. subtract from length keep summing until you get lengths equal length of list
        # 
        # if start pointer ever gets back to 0 answer is  -1
        
        start = 0
        end = 0 
        sum = 0
        length = 0
        while start<len(gas) and length < len(gas):
            sum += gas[end]-cost[end]
            length +=1
            while start<len(gas) and sum < 0:
                sum -= gas[start] - cost[start]
                start +=1
                length-=1
            end+=1
            end = end % len(gas)
        if length == len(gas):
            return start
        return -1
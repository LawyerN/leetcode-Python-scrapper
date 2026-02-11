class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])

        # keep track of the end coordinate of the last balloon we burst
        last_end = float(\'-inf\')
        arrow_count = 0

        for start, end in points:
            # if the current balloon starts before the last one ended,
            # we can burst it with the same arrow
            if start <= last_end:
                last_end = min(last_end, end)
            else:
                # otherwise, we need a new arrow to burst the balloon
                arrow_count += 1
                last_end = end

        return arrow_count
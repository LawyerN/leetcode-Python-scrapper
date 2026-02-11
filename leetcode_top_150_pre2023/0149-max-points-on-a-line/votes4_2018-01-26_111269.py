def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def maxPoints(points):
    slopeMap = dict()
    num_points = len(points)
    maxPoint = 0
    for i in xrange(num_points):
        verticalPoints = overlapPoints = currMax = 0
        for j in xrange(i + 1, num_points):
            print "(" + str(points[i].x) + "," + str(points[i].y) + ") and (" + str(points[j].x) + "," + str(
                points[j].y) + ")",
            if (points[i].x == points[j].x and points[i].y == points[j].y):
                overlapPoints += 1
                print "| OVERLAP |",
            elif points[i].x == points[j].x:
                verticalPoints += 1
                print "| VERT |",
            else:
                print "| NORM |",
                slope = [(points[i].y - points[j].y), (points[i].x - points[j].x)]
                temp = gcd(slope[0], slope[1])
                slope = [slope[0] / temp, slope[1] / temp]
                try:
                    slopeMap[str(slope)] += 1
                except:
                    slopeMap[str(slope)] = 1
                # update the current max - has the current slope value risen to the top?
                print "currMax =", currMax, "but slopeMap[slope] = ", slopeMap[str(slope)],
                currMax = max(currMax, slopeMap[str(slope)])

            # has number of vertical points risen even more?
            currMax = max(currMax, verticalPoints)
            print "currMax =", currMax

        # maxpoint - the maximum number of collinear points with this point
        maxPoint = max(maxPoint, currMax + overlapPoints + 1)
        print " - Max number of points collinear at this stage are", maxPoint
        slopeMap.clear()
    return maxPoint
def maxPoints(self, points: List[List[int]]) -> int:
        def dic():
            return defaultdict(int);
        ans = 0;
        hmap = defaultdict(dic) 
        n = len(points)
        for i in range(0,n):
            print("------------")
            print(f\'i:{i} point[i]:{points[i]} \')
            hmap.clear();
            for j in range(i+1,n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]

                if(  y == 0 ):
                    hmap[0][0] += 1
                    if( hmap[0][0] > ans ):
                        ans = hmap[0][0];
                    continue;
                
                g = gcd(x,y);

                x //= g
                y //= g
                # in case of negative slope one value can be negative (eg)
                # eg (1,-1) and (-1,1) will result in slop m = -1 but here 
                if( y < 0 ):
                    x = -x 
                    y = -y 
                
                hmap[x][y] += 1
                print(f\'j:{j} point[j]:{points[j]} x:{x} y:{y} hmap[{x}][{y}]:{hmap[x][y]}\')
                if( hmap[x][y] > ans ):
                    ans = hmap[x][y];
            
        return ans+1;
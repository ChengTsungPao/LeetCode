class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)<=2): 
            return len(points)
        
        def slope(x1, y1, x2, y2):
            if((x1-x2)==0): 
                return float("inf")
            elif((y1-y2)==0):
                return 0
            else:
                return round((y1-y2)/(x1-x2), 8)
            
        dict = {}
        for i in range(len(points)):
            tmp = set()
            flag = False
            for j in range(len(points)):
                if(points[i]!=points[j]):
                    m = slope(points[i][0], points[i][1], points[j][0], points[j][1])
                    if(abs(m)==float("inf")):
                        b = points[i][0]
                    else:
                        b = round(points[i][1] - m * points[i][0], 5)
                    temp = str(m) + " " + str(b)
                    dict[temp]  = dict.get(temp, 1) + 1
                    tmp.add(temp)
                elif(i!=j):
                    flag = True
            if(flag):
                for k in tmp:
                    dict[k] += 1

        if(dict=={}):
            return len(points)
        else:
            return int(max(dict.values())**0.5) + 1
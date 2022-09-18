class Solution:
   def countOfAtoms(self, formula: str) -> str:
       # find pair of ()
       pairIndex = {}
       stack = []
       for i, ch in enumerate(formula):
           if ch == "(":
               stack.append(i)
           elif ch == ")":
               pairIndex[stack.pop()] = i
               
       # recur
       def merge(d1, d2, times):
           for key in list(d2.keys()):
               d1[key] += d2[key] * times
           return d1
       
       def recur(i, j):
           if i == j:
               return {formula[i]: 1}
           elif i > j:
               return {}
           
           ans = collections.defaultdict(int)
           
           index = i
           while index <= j:
               if formula[index] == "(":
                   leftIndex, rightIndex = index, pairIndex[index]
                   if rightIndex + 1 <= j and formula[rightIndex + 1].isdigit():
                       ret = recur(leftIndex + 1, rightIndex - 1)
                       
                       # find number
                       k = rightIndex + 1
                       number = ""
                       while k <= j and formula[k].isdigit():
                           number += formula[k]
                           k += 1
                           
                       ans = merge(ans, ret, int(number))
                       
                       # update index
                       index = k
                   else:
                       ret = recur(leftIndex + 1, rightIndex - 1)
                       ans = merge(ans, ret, 1)
                       
                       # update index
                       index = rightIndex + 1
               else:
                   _str = formula[index]
                   index += 1
                   while index <= j and 97 <= ord(formula[index]) < 97 + 26:
                       _str += formula[index]
                       index += 1
                   
                   number = "1"
                   if index <= j and formula[index].isdigit():
                       # find number
                       k = index
                       number = ""
                       while k <= j and formula[k].isdigit():
                           number += formula[k]
                           k += 1    
                       
                       # update index
                       index = k

                   ans[_str] += int(number)
                   
           return ans
       
       # sort key
       ans = ""
       status = recur(0, len(formula) - 1)
       for key in sorted(status.keys()):
           ans += key
           if status[key] >= 2:
               ans += str(status[key])

       return ans
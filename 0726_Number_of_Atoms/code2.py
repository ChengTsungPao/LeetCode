class Solution:
   def countOfAtoms(self, formula: str) -> str:

       pairIndex = {}
       stack = []
       for i, ch in enumerate(formula):
           if ch == "(":
               stack.append(i)
           elif ch == ")":
               pairIndex[stack.pop()] = i
       
       def getNumber(k, j):
           if k > j or not formula[k].isdigit():
               return 1, k
           number = ""
           while k <= j and formula[k].isdigit():
               number += formula[k]
               k += 1
           return int(number), k
       
       def getSymbol(i, j):
           symbol = formula[i]
           i += 1
           while i <= j and formula[i].islower():
               symbol += formula[i]
               i += 1
           return symbol, i
       
       def mergeDict(d1, d2, times):
           for key in list(d2.keys()):
               d1[key] += d2[key] * times
           return d1
       
       def recur(i, j):
           if i == j:
               return {formula[i]: 1}
           elif i > j:
               return {}
           
           status = collections.defaultdict(int)
           
           while i <= j:
               if formula[i] == "(":
                   k = pairIndex[i]
                   ret = recur(i + 1, k - 1)
                   number, i = getNumber(k + 1, j)
                   status = mergeDict(status, ret, number)
               else:
                   symbol, i = getSymbol(i, j)
                   number, i = getNumber(i, j)
                   status[symbol] += number
           return status

       ans = ""
       status = recur(0, len(formula) - 1)
       for key in sorted(status.keys()):
           ans += key + str(status[key]) if status[key] >= 2 else key

       return ans
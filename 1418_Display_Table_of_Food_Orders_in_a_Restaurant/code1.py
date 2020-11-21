class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tablenumber = set()
        foodkind = set()
        for i in range(len(orders)):
            tablenumber.add(int(orders[i][1]))
            foodkind.add(orders[i][2])
        tablenumber = list(tablenumber)
        tablenumber.sort()
        foodkind = list(foodkind)
        foodkind.sort()
        foodkind.insert(0, "Table")
        num = ["0" for _ in range(len(foodkind))]
        ans = []
        ans.append(foodkind)
        for i in range(len(tablenumber)):
            num[0] = str(tablenumber[i])
            ans.append(copy.copy(num))
        col = {}
        for i in range(1, len(foodkind)):
            col[foodkind[i]] = i
        row = {}
        for i in range(len(tablenumber)):
            row[str(tablenumber[i])] = i + 1
        for i in range(len(orders)):
            ans[row[orders[i][1]]][col[orders[i][2]]] = str(int(ans[row[orders[i][1]]][col[orders[i][2]]]) + 1)
        return ans
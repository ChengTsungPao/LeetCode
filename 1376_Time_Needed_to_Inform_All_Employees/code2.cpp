class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        int ans = 0;
        vector<vector<int>> graph(n, vector<int>());
        for(int employee = 0; employee < n; employee++){
            if(manager[employee] != -1){
                graph[manager[employee]].push_back(employee);
            }
        }
        return recur(headID, graph, manager, informTime);
    }
    
    int recur(int employee, vector<vector<int>>& graph, vector<int>& manager, vector<int>& informTime) {
        int _max = 0;
        for(int e: graph[employee]){
            _max = max(_max, recur(e, graph, manager, informTime));
        }
        return _max + informTime[employee];
    }
    
};
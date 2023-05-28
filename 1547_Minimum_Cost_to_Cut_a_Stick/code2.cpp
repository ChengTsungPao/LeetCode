class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(), cuts.end());
        
        int m = cuts.size();
        vector<vector<int>> memo(m, vector<int>(m, -1));
        return recur(0, m - 1, cuts, memo);
    }
    
    int recur(int i, int j, vector<int>& cuts, vector<vector<int>>& memo) {   
        if(i + 1 == j) {
            return 0;
        }
        
        if(memo[i][j] != -1){
            return memo[i][j];
        }
        
        int ans = INT_MAX;
        for(int k = i + 1; k < j; k++){
            ans = min(ans, recur(i, k, cuts, memo) + recur(k, j, cuts, memo) + (cuts[j] - cuts[i]));
        }
        memo[i][j] = ans;
        return ans;
    }
    
};
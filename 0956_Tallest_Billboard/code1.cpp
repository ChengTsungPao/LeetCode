class Solution {
public:
    int memo[20 + 1][10000 + 1];
    
    int tallestBillboard(vector<int>& rods) {
        int n = rods.size();
        memset(memo, -1, sizeof(memo));
        return recur(0, 0, rods);
    }
    
    int recur(int idx, int sub, vector<int>& rods){
        int n = rods.size();
        if (idx >= n) {
            return (sub == 0) ? 0 : INT_MIN;
        }
        
        if(memo[idx][sub + 5000] != -1){
            return memo[idx][sub + 5000];
        }
        
        int rod = rods[idx];
        int g1 = recur(idx + 1, sub + rod, rods);
        int g2 = recur(idx + 1, sub - rod, rods);
        int g3 = recur(idx + 1, sub, rods);
        
        g1 = (g1 != INT_MIN) ? g1 + rod : INT_MIN;
        int ans = max(g1, max(g2, g3));
        
        memo[idx][sub + 5000] = ans;
        return ans;
    }
    
};
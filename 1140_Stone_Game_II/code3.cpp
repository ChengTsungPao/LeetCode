class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<vector<vector<int>>> memo(n, vector<vector<int>>(n + 1, vector<int>(2, -1)));
        return recur(0, 1, true, piles, memo);
    }
    
    int recur(int idx, int M, bool who, vector<int>& piles, vector<vector<vector<int>>>& memo) {
        int n = piles.size();
        if(idx >= n){
            return 0;
        }
        
        if(memo[idx][M][who] != -1){
            return memo[idx][M][who];
        }
        
        int ans = (who) ? INT_MIN : INT_MAX, _sum = 0;
        if(who){
            for(int x = 1; x <= min(2 * M, n - idx); x++){
                _sum += piles[idx + x - 1];
                ans = max(ans, recur(idx + x, max(x, M), false, piles, memo) + _sum);
            }
        } else {
            for(int x = 1; x <= min(2 * M, n - idx); x++){
                _sum += piles[idx + x - 1];
                ans = min(ans, recur(idx + x, max(x, M), true, piles, memo));
            }
        }
        
        memo[idx][M][who] = ans;
        return ans;
    }
    
};
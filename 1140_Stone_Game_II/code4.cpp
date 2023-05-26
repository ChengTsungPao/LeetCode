class Solution {
public:
    int stoneGameII(vector<int>& piles) {
	// 計算 Alice - Bob 和 Alice + Bob，解出 Alice

        int n = piles.size();
        int _sum = accumulate(piles.begin(), piles.end(), 0);
        vector<vector<int>> memo(n, vector<int>(n + 1, -1));
        return (_sum + recur(0, 1, piles, memo)) / 2;
    }
    
    int recur(int idx, int M, vector<int>& piles, vector<vector<int>>& memo) {
        int n = piles.size();
        if(idx >= n){
            return 0;
        }
        
        if(memo[idx][M] != -1){
            return memo[idx][M];
        }
        
        int ans = INT_MIN, _sum = 0;
        for(int x = 1; x <= min(2 * M, n - idx); x++){
            _sum += piles[idx + x - 1];
            ans = max(ans, _sum - recur(idx + x, max(x, M), piles, memo));
        }
        
        memo[idx][M] = ans;
        return ans;
    }
    
};
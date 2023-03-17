class Solution {
public:
    int waysToReachTarget(int target, vector<vector<int>>& types) {
        vector<vector<int>> memo(types.size() + 1, vector<int>(target + 1, -1));
        int MOD = pow(10, 9) + 7;
        return recur(0, target, types, memo, MOD);
    }
    
    int recur(int idx, int target, vector<vector<int>>& types, vector<vector<int>>& memo, int MOD){
        if(target == 0){
            return 1;
        } else if (target < 0 || idx >= types.size()){
            return 0;
        }
        
        if(memo[idx][target] != -1){
            return memo[idx][target];
        }
        
        int ans = 0;
        int val = types[idx][1];
        int count = types[idx][0];
        for(int i = 0; i <= count; i++){
            ans += recur(idx + 1, target - val * i, types, memo, MOD) % MOD;
            ans %= MOD;
        }
        
        memo[idx][target] = ans;
        return ans;
    }
};
class Solution {
public:
    int memo[1001];
    
    int combinationSum4(vector<int>& nums, int target) {
        memset(memo, -1, sizeof(memo));
        return recur(target, nums);
    }
    
    int recur(int target, vector<int>& nums){
        int n = nums.size();
        
        if(target <= 0){
            return target == 0;
        }
        
        if(memo[target] != -1){
            return memo[target];
        }
        
        int ans = 0;
        for(int num: nums){
            ans += recur(target - num, nums);
        }
        return memo[target] = ans;
    }
    
};
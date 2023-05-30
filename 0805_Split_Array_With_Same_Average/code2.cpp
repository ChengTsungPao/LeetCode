class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums) {
        int n = nums.size();
        int _sum = accumulate(nums.begin(), nums.end(), 0);
        vector<vector<vector<int>>> memo(n + 1, vector<vector<int>>(n / 2 + (n % 2) + 1, vector<int>(_sum + 1, -1)));
        return recur(0, 0, 0, _sum, nums, memo);
    }
    
    bool recur(int idx, int A, int A_len, int _sum, vector<int>& nums, vector<vector<vector<int>>>& memo){
        int n = nums.size();
        if(A_len > 0 && A_len < n && A * (n - A_len) == (_sum - A) * A_len){
            return true;
        } else if (idx >= n || A_len > n / 2 + (n % 2)){
            return false;
        }
        
        if(memo[idx][A_len][A] != -1){
            return memo[idx][A_len][A];
        }
        
        memo[idx][A_len][A] = recur(idx + 1, A, A_len, _sum, nums, memo) || recur(idx + 1, A + nums[idx], A_len + 1, _sum, nums, memo);
        return memo[idx][A_len][A];
    }
    
};
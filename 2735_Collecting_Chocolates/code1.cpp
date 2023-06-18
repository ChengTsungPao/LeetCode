class Solution {
public:
    long long minCost(vector<int>& nums, int x) {
        // r = 0
        // [20, 1, 15]
        //  20  1  15 => 20 + 1 + 15 => 36
        
        // r = 1
        // [20, 1, 15]
        //  20  1  15
        //  15 20   1 => 15 + 1 + 1 + 5 * 1 => 22
        
        // r = 2
        // [20, 1, 15]
        //  20  1  15
        //  15 20   1 => 15 + 1 + 15 => 31
        //  20  1  15
        //   1 15  20 => 1 + 1 + 1 + 5 * 2 => 13
        
        long long ans = LLONG_MAX;
        int n = nums.size();
        vector<int> minCost = nums;
        
        for(int r = 0; r <= n - 1; r++){
            long long total_cost = accumulate(minCost.begin(), minCost.end(), (long long)0);
            total_cost += (long long)x * r;
            ans = min(ans, total_cost);
            
            for(int k = 0; k < n; k++){
                minCost[k] = min(minCost[k], nums[((r + 1) + k) % n]);
            }
        }
        
        return ans;
    }
};
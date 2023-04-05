class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        // Main Idea: if i < j => nums[i] + 1 & nums[j] - 1 (Not just near index)
        
        // binary search
        int ans = pow(10, 9);
        int left = 0, right = pow(10, 9);
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(condition(mid, nums)){
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
                
        }

        return ans;
    }
    
    bool condition(int target, vector<int>& nums){
        if(target < nums[0]) return false;
        long long remainder_inc = 0;
        int n = nums.size();
        for(int i = n - 1; i >= 0; i--){
            remainder_inc += nums[i] - target;
            remainder_inc = (remainder_inc >= 0) ? remainder_inc : 0;
        }
        return remainder_inc == 0;
    }
    
};
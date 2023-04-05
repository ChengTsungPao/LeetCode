class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        // Main Idea: if i < j => nums[i] + 1 & nums[j] - 1 (Not just near index)
        
        int n = nums.size();
        
        // operate first two number
        if(nums[0] < nums[1]){
            long long sum = nums[0] + nums[1];
            nums[0] = sum / 2 + sum % 2;
            nums[1] = sum / 2;
        }
        
        // operate other number
        int cur_max = max(nums[0], nums[1]);
        long long remaider_inc = cur_max * 2 - (nums[0] + nums[1]);
        for(int i = 2; i < n; i++){
            int num = nums[i];
            if(num <= cur_max){
                remaider_inc += cur_max - num;
            } else if (num - cur_max <= remaider_inc) {
                remaider_inc -= num - cur_max;
            } else {
                long long need_inc = num - cur_max - remaider_inc;
                int new_cur_max = cur_max + need_inc / (i + 1) + (need_inc % (i + 1) > 0);
                
                remaider_inc = (new_cur_max - cur_max) * (i + 1) - need_inc;
                cur_max = new_cur_max;
            }
        }
        
        return cur_max;
    }
};
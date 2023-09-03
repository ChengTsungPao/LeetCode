class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        
        // "same" num combine to bigger num
        long long sum = accumulate(nums.begin(), nums.end(), (long long)0);
        if(sum < target){
            return -1;
        }
        
        sort(nums.begin(), nums.end());
        
        int ans = 0;
        while(!nums.empty() && target > 0){
            int num = nums.back(); nums.pop_back();
            
            // sum    = 11100
            // num    = 10000
            // target = 01011
            if(sum - num >= target){
                sum -= num;
                
            // sum    = X1100
            // num    = X1000
            // target = X1011
            } else if (num <= target){
                sum -= num;
                target -= num;
                
            // sum    = XX100
            // num    = XX100
            // target = XX011
            } else {
                nums.push_back(num / 2);
                nums.push_back(num / 2);
                ans++;
            }
        }
        
        return ans;
    }
};
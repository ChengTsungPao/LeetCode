class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        
        long long ans = 0, count = 0;
        
        for(int num: nums){
            count = (num == 0) ? count + 1 : 0;
            ans += count;
        }
        
        return ans;
    }
};
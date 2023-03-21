class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        
        long long ans = 0, count = 0;
        
        for(int num: nums){
            if(num == 0){
                count += 1;
            } else {
                ans += (count + 1) * count / 2;
                count = 0;
            }
        }
        ans += (count + 1) * count / 2;
        
        return ans;
    }
};
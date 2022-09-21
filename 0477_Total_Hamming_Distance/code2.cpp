class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        
        int ans = 0;
        int sum = 0;
        
        while(!isAllZeros(nums)){
            for(int i = 0; i < nums.size(); i++){
                ans += nums[i] & 1 ? i - sum : sum;
                sum += nums[i] & 1;
                nums[i] >>= 1;
            }
            sum = 0;
        }

        return ans;
    }
    
    bool isAllZeros(vector<int>& nums){
        for(int num: nums){
            if(num > 0){
                return false;
            } 
        }
        return true;
    }
};
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        unsigned int ans = 0;
        for(unsigned int i = 0; i < nums.size(); i++){
            for(unsigned int j = i + 1; j < nums.size(); j++){
                ans += countBit(nums[i] ^ nums[j]);
            }            
        }
        return ans;
    }
    
    int countBit(int num){
        int ans = 0;
        while(num > 0){
            ans += num % 2;
            num /= 2;
        }
        return ans;
    }
};
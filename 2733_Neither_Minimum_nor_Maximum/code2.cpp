class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        int n = nums.size();
        if(n <= 2){
            return -1;
        }
        
        sort(nums.begin(), nums.begin() + 3);
        return nums[1];
    }
};
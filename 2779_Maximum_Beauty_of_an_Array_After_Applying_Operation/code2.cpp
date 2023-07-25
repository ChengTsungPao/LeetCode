class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        int ans = 0;
        int i = 0;
        for(int j = 0; j < n; j++){
            while(i < j && nums[j] - nums[i] > 2 * k){
                i += 1;
            }
            ans = max(ans, j - i + 1);
        }
        
        return ans;
    }
};
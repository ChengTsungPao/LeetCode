class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n - 2; i++){
            if(i > 0 and nums[i] == nums[i - 1]){
                continue;
            }
            
            int j = i + 1, k = n - 1;
            while(j < k){
                if(nums[i] + nums[j] * 2 > 0 || nums[i] + nums[k] * 2 < 0){
                    break;
                }
                
                if(nums[i] + nums[j] + nums[k] < 0){
                    j++;
                } else if (nums[i] + nums[j] + nums[k] > 0){
                    k--;
                } else {
                    ans.push_back({nums[i], nums[j], nums[k]});
                    while(j < k and nums[j] == nums[j + 1]) j++;
                    while(j < k and nums[k - 1] == nums[k]) k--;
                    j++; k--;
                }
            }
        }
        
        return ans;
    }
};
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) {
            return {};
        }
        
        vector<string> ans;
        int start = nums[0], end = nums[0];
        for(int i = 0; i < n; i++){
            end = nums[i];
            if(i + 1 >= n || nums[i] + 1 != nums[i + 1]){
                ans.push_back((start == end) ? to_string(start) : to_string(start) + "->" + to_string(end));
                start = (i + 1 < n) ? nums[i + 1] : start;
            }
        }
        
        return ans;
    }
};
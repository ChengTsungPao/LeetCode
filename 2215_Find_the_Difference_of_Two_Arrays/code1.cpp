class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> nums1_set(nums1.begin(), nums1.end());
        unordered_set<int> nums2_set(nums2.begin(), nums2.end());
        
        vector<vector<int>> ans(2, vector<int>());
        for(int num: nums1_set){
            if(nums2_set.find(num) == nums2_set.end()) ans[0].push_back(num);
        }
        for(int num: nums2_set){
            if(nums1_set.find(num) == nums1_set.end()) ans[1].push_back(num);
        }
        
        return ans;
    }
};
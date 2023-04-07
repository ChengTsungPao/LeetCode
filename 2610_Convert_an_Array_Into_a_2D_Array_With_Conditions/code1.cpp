class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        
        int n = nums.size();
        
        int maxCount = 0;
        vector<int> count(201, 0);
        for(int num: nums){
            count[num] += 1;
            maxCount = max(maxCount, count[num]);
        }
        
        vector<vector<int>> ans(maxCount, vector<int>());
        for(int num = 1; num < 201; num++){
            while(count[num]){
                count[num]--;
                ans[count[num]].push_back(num);
            }
        }
        
        return ans;
    }
};
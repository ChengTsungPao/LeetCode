class Solution {
public:
    unordered_map<int, vector<vector<int>>> memo;
    
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> ans;
        for(auto v: recur(nums, 0)){
            if(v.size() > 1){
                ans.push_back(v);
            }
        }
        return ans;
    }
    
    vector<vector<int>> recur(vector<int>& nums, int idx) {
        
        if(memo.find(idx) == memo.end()){
        
            if(idx >= nums.size()){
                return {};
            }

            vector<vector<int>> ret;
            unordered_set<int> cache;

            for(unsigned int i = idx; i < nums.size(); i++){
                if(cache.find(nums[i]) != cache.end()){
                    continue;
                }

                cache.insert(nums[i]);
                ret.push_back({nums[i]});
                for(auto v: recur(nums, i + 1)){
                    if(nums[i] <= v[0]){
                        v.insert(v.begin(), nums[i]);
                        ret.push_back(v);
                    }
                }
            }
            
            memo[idx] = ret;
        }
        
        return memo[idx];
    }
    
};
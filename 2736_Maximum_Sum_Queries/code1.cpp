class Solution {
public:
    vector<int> maximumSumQueries(vector<int>& nums1, vector<int>& nums2, vector<vector<int>>& queries) {
        
        int m = queries.size();
        map<int, set<tuple<int, int>>> numsMap;  
        for(int i = 0; i < m; i++){
            int x = queries[i][0], y = queries[i][1];
            numsMap[x].insert({y, i});
        }        
        
        int n = nums1.size();
        vector<vector<int>> nums_merge;
        for(int i = 0; i < n; i++){
            nums_merge.push_back({nums1[i] + nums2[i], nums1[i], nums2[i]});
        }
        sort(nums_merge.rbegin(), nums_merge.rend());
        
        vector<int> ans(m, -1);
        for(auto& num: nums_merge){
            int add = num[0], num1 = num[1], num2 = num[2];
            
            auto it = numsMap.begin();
            while(it != numsMap.end()){
                
                int x = it -> first;
                if(x > num1){
                    break;
                }
                
                set<tuple<int, int>> s = it -> second;
                for(auto& t: s){
                    int y = get<0>(t), i = get<1>(t);
                    if(y > num2){
                        break;
                    }
                    
                    ans[i] = add;
                    numsMap[x].erase(t);
                }
                
                if(numsMap[x].size() == 0) {
                    numsMap.erase(it++);
                } else {
                    it++;
                }
            }
        }
        
        return ans;
    }
};
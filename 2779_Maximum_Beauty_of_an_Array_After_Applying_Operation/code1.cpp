class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        /*
        k = 2
        [4,6, 1,2]
         2 4 -1 0
         6 8  3 4
        */
        
        vector<tuple<int, int>> arr;
        for(int num: nums){
            arr.push_back({num - k, -1});
            arr.push_back({num + k, 1});
        }
        
        sort(arr.begin(), arr.end());
        
        int ans = 0;
        int cur = 0;
        for(auto t: arr){
            int target = get<1>(t);
            cur += -target;
            ans = max(ans, cur);
        }
        return ans;
    }
};
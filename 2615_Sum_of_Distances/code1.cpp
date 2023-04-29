class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();   
        unordered_map<int, long long> numSumIdx;
        unordered_map<int, vector<int>> numIdx;

        for(int i = 0; i < n; i++){
            int num = nums[i];
            numIdx[num].push_back(i);
            numSumIdx[num] += i;
        }
        
        vector<long long> ans(n, 0);
        for(auto it = numIdx.begin(); it != numIdx.end(); it++){
            int num = it -> first;
            int m = numIdx[num].size();
            long long sum = numSumIdx[num];
            
            int idx = numIdx[num][0];
            ans[idx] = sum - idx * m;
            for(int i = 1; i < m; i++){
                int idx1 = numIdx[num][i - 1], idx2 = numIdx[num][i];
                ans[idx2] = ans[idx1] + (idx2 - idx1) * i - (idx2 - idx1) * (m - i);
            }
        }
        
        return ans;
    }
};
class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int n = nums.size();
        
        long long total = 0;
        vector<tuple<int, int>> nums_cost;
        for(int i = 0; i < n; i++){
            nums_cost.push_back({nums[i], cost[i]});
            total += cost[i];
        }
        sort(nums_cost.begin(), nums_cost.end());
        
        int median = 0;
        long long order = 0;
        for(int i = 0; i < n; i++){
            tuple<int, int> t = nums_cost[i];
            int num = get<0>(t), c = get<1>(t);
            order += c;
            if(order >= total / 2 + 1){
                median = num;
                break;
            }
        }
        
        long long ans = 0;
        for(int i = 0; i < n; i++){
            ans += (long long)cost[i] * abs(nums[i] - median);
        }
        
        return ans;
    }
};
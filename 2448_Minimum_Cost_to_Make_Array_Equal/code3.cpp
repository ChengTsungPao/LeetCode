class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int n = nums.size();
        
        long long prefixCost = 0, suffixCost = 0, total_cost = 0;
        vector<tuple<int, int>> nums_cost;
        for(int i = 0; i < n; i++){
            int num = nums[i], c = cost[i];
            suffixCost += c;
            total_cost += (long long)num * c;
            nums_cost.push_back({num, c});
        }
        sort(nums_cost.begin(), nums_cost.end());
        
        int preNum = 0;
        long long ans = total_cost;
        for(int i = 0; i < n; i++){
            tuple<int, int> t = nums_cost[i];
            int num = get<0>(t), c = get<1>(t);
            
            int gap = num - preNum;
            total_cost -= gap * suffixCost;
            total_cost += gap * prefixCost;
            ans = min(ans, total_cost);

            prefixCost += c;
            suffixCost -= c;
            preNum = num;
        }
        
        return ans;
    }
};
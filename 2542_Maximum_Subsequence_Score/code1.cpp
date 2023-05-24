class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        
        vector<tuple<int, int>> nums;
        for(int i = 0; i < n; i++){
            nums.push_back({nums2[i], nums1[i]});
        }
        
        sort(nums.begin(), nums.end(), greater<tuple<int, int>>());
        
        priority_queue<int, vector<int>, greater<int>> pq;
        long long ans = 0, _sum = 0;
        for(int i = 0; i < n; i++){
            tuple<int, int> t = nums[i];
            int num2 = get<0>(t), num1 = get<1>(t);
            
            if(pq.size() == k - 1){
                ans = max(ans, (_sum + num1) * num2);
            }
            
            _sum += num1;
            pq.push(num1);
            if(pq.size() >= k){
                _sum -= pq.top(); pq.pop();
            }
        }
        
        return ans;        
    }
};
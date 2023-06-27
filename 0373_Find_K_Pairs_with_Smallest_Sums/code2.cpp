class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        int m = nums2.size();
        
        vector<int> index(n, 0);
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        for(int i = 0; i < n; i++){
            int j = index[i];
            if(j < m){
                pq.push({nums1[i] + nums2[j], i, j});
                index[i]++;
            }
        }
        
        vector<vector<int>> ans;
        while(k > 0 && !pq.empty()){
            tuple<int, int, int> t = pq.top(); pq.pop();
            int i = get<1>(t), j = get<2>(t);
            ans.push_back({nums1[i], nums2[j]});
            
            j = index[i];
            if(j < m){
                pq.push({nums1[i] + nums2[j], i, j});
                index[i]++;
            }
            k--;
        }
        
        return ans;
    }
};
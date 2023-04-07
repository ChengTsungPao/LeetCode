class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        
        int n = reward1.size();
        
        vector<tuple<int, int>> sub;
        for(int i = 0; i < n; i++){
            sub.push_back({reward2[i] - reward1[i], i});
        }
        
        sort(sub.begin(), sub.end());
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            tuple<int, int> t = sub[i];
            int idx = get<1>(t);
            ans += (i < k) ? reward1[idx] : reward2[idx];
        }
        
        return ans;        
    }
};
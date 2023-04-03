class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        
        int n = s.size();
        
        // cal abs(s[i] - t[i]) prefix sum
        vector<int> prefix(n, 0);
        prefix[0] = abs(s[0] - t[0]);
        for(int i = 1; i < n; i++){
            prefix[i] = prefix[i - 1] + abs(s[i] - t[i]);
        }
        
        // get upperbound by binary search
        int ans = 0;
        for(int i = 0; i < n; i++){
            int upperVal = (i > 0) ? maxCost + prefix[i - 1] : maxCost;
            int j = upper_bound(prefix.begin(), prefix.end(), upperVal) - prefix.begin();
            ans = max(ans, j - i);
        }
        
        return ans;
    }
};
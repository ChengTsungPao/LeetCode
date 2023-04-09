class Solution {
public:
    int maximizeWin(vector<int>& prizePositions, int k) {
        
        int n = prizePositions.size();
        int i, j;
        
        // prefix[j] => 0 ~ j max segment
        vector<int> prefix(n, 1);
        i = 0;
        for(j = 1; j < n; j++){
            while(prizePositions[j] - prizePositions[i] > k) i++;
            prefix[j] = max(prefix[j - 1], j - i + 1);
        }
        
        // suffix[i] => i ~ n - 1 max segment
        vector<int> suffix(n, 1);
        j = n - 1;
        for(i = n - 2; i >= 0; i--){
            while(prizePositions[j] - prizePositions[i] > k) j--;
            suffix[i] = max(suffix[i + 1], j - i + 1);
        }
        
        int ans = 0;
        for(i = 0; i < n; i++){
            ans = max(ans, (i > 0) ? (prefix[i - 1] + suffix[i]) : suffix[i]);
        }
        
        return ans;
    }
};
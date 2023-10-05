class Solution {
public:
    long long maximumSumOfHeights(vector<int>& maxHeights) {
        int n = maxHeights.size();

        long long ans = 0;
        for(int i = 0; i < n; i++){
            int h = maxHeights[i];
            long long s = h;
            for(int j = i + 1; j < n; j++){
                h = min(h, maxHeights[j]);
                s += h;
            }
            h = maxHeights[i];
            for(int j = i - 1; j >= 0; j--){
                h = min(h, maxHeights[j]);
                s += h;
            }
            ans = max(ans, s);
        }
        
        return ans;
    }
};
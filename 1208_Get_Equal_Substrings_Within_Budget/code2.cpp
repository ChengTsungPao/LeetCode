class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int i = 0, sum = 0, ans = 0;
        for(int j = 0; j < s.size(); j++){
            sum += abs(s[j] - t[j]);
            while(i <= j && sum > maxCost){
                sum -= abs(s[i] - t[i]);
                i += 1;
            }
            ans = max(ans, j - i + 1);
        }
        return ans;
    }
};
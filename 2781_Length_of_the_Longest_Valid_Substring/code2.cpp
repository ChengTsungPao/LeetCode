class Solution {
public:
    int longestValidSubstring(string word, vector<string>& forbidden) {
        
        int n = word.size();
        unordered_set<string> forbidden_set(forbidden.begin(), forbidden.end());
        
        int ans = 0;
        int i = -1;
        for(int j = 0; j < n; j++){
            string cur_s = "";
            for(int k = j; k > max(j - 10, i); k--){
                cur_s = word[k] + cur_s;
                if(forbidden_set.find(cur_s) != forbidden_set.end()){
                    i = k;
                    break;
                }
            }
            
            ans = max(ans, j - i);
        }
        
        return ans;
    }
};
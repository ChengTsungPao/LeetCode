class Solution {
public:
    int minDeletions(string s) {        
        unordered_map<int, int> freq;
        vector<int> count(26, 0);
        for(char c: s){
            count[c - 'a']++;
        }
        
        int max_f = 0;
        for(int i = 0; i < 26; i++){
            int f = count[i];
            freq[f]++;
            max_f = max(max_f, f);
        }
        
        int ans = 0;
        for(int f = max_f; f >= 1; f--){
            int del = (freq[f] > 0) ? (freq[f] - 1) : 0;
            ans += del;
            freq[f - 1] += del;
        }
        
        return ans;
    }
};
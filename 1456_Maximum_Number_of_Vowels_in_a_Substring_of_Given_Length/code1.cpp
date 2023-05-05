class Solution {
public:
    int maxVowels(string s, int k) {
        int ans = 0;
        
        vector<int> count(5, 0);
        unordered_map<char, int> idx = {{'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}};
        for(int i = 0; i < s.size(); i++){
            if(idx.find(s[i]) != idx.end()) count[idx[s[i]]]++;
            if(i + 1 >= k){
                ans = max(ans, *max_element(count.begin(), count.end()));
                if(idx.find(s[i - k + 1]) != idx.end()) count[idx[s[i - k + 1]]]--;
            }
            
        }
        
        return ans;
    }
};
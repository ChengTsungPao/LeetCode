class Solution {
public:
    int ans = 1;
    
    int maxUniqueSplit(string s) {
        int n = s.size();
        unordered_set<string> cache;
        string cur_s = "";
        backtrack(0, cur_s, s, cache);
        return ans;
    }
    
    void backtrack(int i, string& cur_s , string& s, unordered_set<string>& cache){
        int n = s.size();
        if(i >= n){
            if(cache.find(cur_s) == cache.end()) ans = max(ans, (int)cache.size() + (!cur_s.empty()));
            return;
        }
        
        cur_s.push_back(s[i]);
        
        // non-split
        backtrack(i + 1, cur_s, s, cache);
        
        // split
        if(cache.find(cur_s) == cache.end()){
            cache.insert(cur_s);
            string nxt_s = "";
            backtrack(i + 1, nxt_s, s, cache);
            cache.erase(cur_s);
        }
        
        cur_s.pop_back();
    }
    
};
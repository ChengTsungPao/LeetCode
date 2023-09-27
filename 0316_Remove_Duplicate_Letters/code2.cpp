class Solution {
public:
    string removeDuplicateLetters(string s) {
        int n = s.size();
        
        vector<bool> cache(26, false);
        vector<int> last(26, 0);
        for(int i = 0; i < n; i++){
            char ch = s[i];
            last[ch - 'a'] = max(last[ch - 'a'], i);
        }
        
        string stack;
        for(int i = 0; i < n; i++){
            char ch = s[i];
            if(cache[ch - 'a']){
                continue;
            }
            
            while(!stack.empty() && stack.back() > ch && last[stack.back() - 'a'] > i){
                cache[stack.back() - 'a'] = false;
                stack.pop_back();
            }
            stack.push_back(ch);
            cache[ch - 'a'] = true;
        }
        
        return stack;        
    }
};
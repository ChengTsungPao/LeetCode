class Solution {
public:
    string reorderSpaces(string text) {
        
        int count = 0;
        string word = "";
        vector<string> words;
        for(auto ch: text){
            if(ch == ' '){
                count++;
                if(!word.empty()) words.push_back(word);
                word = "";
            } else {
                word.push_back(ch);
            }
        }
        if(!word.empty()) words.push_back(word);
        
        int n = words.size();
        if(n == 1){
            return words[0] + string(count, ' ');
        }
        
        int q = count / (n - 1), r = count % (n - 1);
        string ans = words[0];
        for(int i = 1; i < n; i++){
            ans += string(q, ' ');
            ans += words[i];
        }
        ans += string(r, ' ');
        return ans;
    }
};
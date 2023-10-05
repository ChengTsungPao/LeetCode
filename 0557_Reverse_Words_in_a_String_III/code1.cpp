class Solution {
public:
    string reverseWords(string s) {
        s += ' ';
        int n = s.size();
        
        string ans;
        for(int i = 0; i < n; i++){
            if(s[i] == ' '){
                int j = i - 1;
                while(j >= 0 && s[j] != ' '){
                    ans.push_back(s[j]);
                    j--;
                }
                ans.push_back(' ');
            }
        }
        ans.pop_back();
        return ans;
    }
};
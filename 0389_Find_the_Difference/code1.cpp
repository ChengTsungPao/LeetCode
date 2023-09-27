class Solution {
public:
    char findTheDifference(string s, string t) {
        int n = s.size();
        
        vector<int> count(26, 0);
        for(int i = 0; i < n; i++){
            count[s[i] - 'a']--;
            count[t[i] - 'a']++;
        }
        count[t[n] - 'a']++;
        
        for(int a = 0; a < 26; a++){
            if(count[a] == 1){
                return a + 'a';
            }
        }
        
        return '#';
    }
};
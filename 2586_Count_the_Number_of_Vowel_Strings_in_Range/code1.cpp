class Solution {
public:
    int vowelStrings(vector<string>& words, int left, int right) {
        unordered_set<char> isVowelCh = {'a', 'e', 'i', 'o', 'u'} ;
        
        int ans = 0;
        for(int i = left; i <= right; i++){
            string word = words[i];
            int n = word.size();
            ans += isVowelCh.count(word[0]) > 0 && isVowelCh.count(word[n - 1]) > 0;
        }
        
        return ans;        
    }
};
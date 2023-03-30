class Solution {
public:
    unordered_map<string, unordered_set<string>> memo;
    
    bool isScramble(string s1, string s2) {
        
        int n = s1.size();
        
        vector<int> count1(26, 0), count2(26, 0);
        for(int i = 0; i < n; i++){
            int ch1 = s1[i], ch2 = s2[i];
            count1[ch1 - 'a'] += 1;
            count2[ch2 - 'a'] += 1;
        }
        
        return isSame(count1, count2) && recur(s1, s2);
    }
    
    bool recur(string s1, string s2){
        
        if(memo[s1].find(s2) != memo[s1].end()){
            return false;
        }
        
        int n = s1.size();
        
        if(n <= 1){
            return true;
        }
        
        vector<int> count1(26, 0), count2(26, 0);
        
        for(int k = 0; k < n; k++){
            int ch1 = s1[k], ch2 = s2[k];
            count1[ch1 - 'a'] += 1;
            count2[ch2 - 'a'] += 1;
            
            if(k != n - 1 && isSame(count1, count2) && recur(s1.substr(0, k + 1), s2.substr(0, k + 1)) && recur(s1.substr(k + 1, n - k - 1), s2.substr(k + 1, n - k - 1))){
                return true;
            }
            
        }
        
        for(int k = 0; k < n; k++){
            int ch1 = s1[k], ch2 = s2[n - k - 1];
            count1[ch1 - 'a'] -= 1;
            count2[ch2 - 'a'] -= 1;
            
            if(k != n - 1 && isSame(count1, count2) && recur(s1.substr(0, k + 1), s2.substr(n - k - 1, k + 1)) && recur(s1.substr(k + 1, n - k - 1), s2.substr(0, n - k - 1))){
                return true;
            }
            
        }
        
        memo[s1].insert(s2);
        return false;
    }
    
    
    bool isSame(vector<int> count1, vector<int> count2){
        for(int i = 0; i < 26; i++){
            if(count1[i] != count2[i]){
                return false;
            }
        }
        return true;
    }
    
};
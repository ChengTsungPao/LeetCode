class Solution {
public:
    string smallestString(string s) {
        int n = s.size();
        
        int start = -1;
        for(int i = 0; i < n; i++) {
            if(s[i] != 'a') {
                start = i;
                break;
            }
        }
        
        if(start == -1){
            s[n - 1] = 'z';
            return s;
        }
        
        int end = n - 1;
        for(int i = start; i < n; i++) {
            if(s[i] == 'a') {
                end = i - 1;
                break;
            }
        }
        
        for(int i = start; i <= end; i++){
            s[i]--;
        }
        
        return s;
    }
};